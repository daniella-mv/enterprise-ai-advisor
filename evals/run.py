import json, time, csv, os, statistics
from typing import List
from app.rag.ingest import main as build_index
from app.rag.retrieve import retrieve_topk

CASES = os.path.join(os.path.dirname(__file__), "cases.jsonl")
OUT = os.path.join(os.path.dirname(__file__), "metrics.csv")

def answer(question: str) -> dict:
    # Minimal answer using retrieve_topk directly (bypass HTTP)
    t0 = time.time()
    chunks = retrieve_topk(question, k=3)
    text = " ".join([c["text"] for c in chunks])
    citations = [c["source"] for c in chunks]

    # --- NEW: simple "don't guess" guard for uncovered topics ---
    # Heuristic: if top score is tiny OR there's almost no word overlap, declare insufficient sources
    top_score = max([c.get("score", 0.0) for c in chunks] or [0.0])
    q_words = set(w.lower().strip(".,!?") for w in question.split())
    overlap = any(any(w in c["text"].lower() for w in q_words) for c in chunks)

    if top_score < 0.01 or not overlap:
        text += "\n\nI cannot answer due to insufficient sources; I will not guess."

    latency = time.time() - t0
    return {"text": text, "citations": citations, "latency": latency}


def passed(text: str, citations: list, keywords: List[str], require_citation: bool):
    t = text.lower()
    ok_kw = all(k.lower() in t for k in keywords)
    ok_ct = (len(citations) > 0) if require_citation else True
    return ok_kw and ok_ct

def run():
    build_index()
    rows, lats = [], []
    total, good = 0, 0
    for line in open(CASES, "r", encoding="utf-8"):
        total += 1
        case = json.loads(line)
        res = answer(case["question"])
        ok = passed(res["text"], res["citations"], case["expected_keywords"], case["require_citation"])
        good += int(ok)
        lats.append(res["latency"])
        rows.append({"id": case["id"], "passed": ok, "latency": round(res["latency"],3), "num_citations": len(res["citations"])})
    p50 = round(statistics.median(lats),3) if lats else 0.0
    rate = round(100.0*good/max(total,1),1)
    print(f"Pass-rate: {rate}% | P50 latency: {p50}s | Cases: {total}")
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["id","passed","latency","num_citations"])
        w.writeheader(); w.writerows(rows)
    print("Wrote", OUT)

if __name__ == "__main__":
    run()

