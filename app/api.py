from fastapi import FastAPI
from pydantic import BaseModel
from app.rag.retrieve import retrieve_topk
from app.guards.redaction import redact_pii
import re

app = FastAPI(title="Enterprise AI Advisor (Demo)")

# --- injection detection ---
INJECTION_TRIGGERS = [
    r"ignore (all )?polic(y|ies)",
    r"override(s)? the rules",
    r"output raw .* without citation",
    r"print env vars",
    r"secret keys?",
]
def is_injection(q: str) -> bool:
    ql = q.lower()
    return any(re.search(p, ql) for p in INJECTION_TRIGGERS)

class AskRequest(BaseModel):
    question: str
    top_k: int = 3
    strict_json: bool = False

class AskResponse(BaseModel):
    answer: str
    citations: list[str]
    meta: dict

@app.post("/ask", response_model=AskResponse)
def ask(req: AskRequest):
    # Block prompt injection
    if is_injection(req.question):
        deny = (
            "Request denied due to prompt-injection risk. "
            "I won’t bypass safety rules or expose secrets."
        )
        return AskResponse(answer=deny, citations=[], meta={"blocked":"injection"})

    # Retrieve sources
    chunks = retrieve_topk(req.question, k=req.top_k)

    # Don’t guess if we have no sources
    if not chunks:
        answer = ("I don’t have sufficient sources to answer confidently. "
                  "I will not guess without citations.")
        return AskResponse(answer=answer, citations=[], meta={"strict_json": req.strict_json})

    # Draft answer from top chunks
    bullets = "\n".join([f"- {c['text'][:220]}..." for c in chunks])
    answer = (
        "Here is what I found:\n"
        f"{bullets}\n\n"
        "If sources are insufficient, I will not guess."
    )
    answer = redact_pii(answer)
    citations = [c["source"] for c in chunks]
    meta = {"scores": [c["score"] for c in chunks], "strict_json": req.strict_json}
    return AskResponse(answer=answer, citations=citations, meta=meta)

@app.get("/health")
def health():
    return {"ok": True}

