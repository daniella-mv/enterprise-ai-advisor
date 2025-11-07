![Eval Gate](https://github.com/daniella-mv/enterprise-ai-advisor/actions/workflows/ci.yml/badge.svg)

# Enterprise AI Advisor — Starter Repo

A minimal, runnable scaffold showing an enterprise-style GenAI/RAG advisor:
- **FastAPI** microservice with a mocked RAG (TF‑IDF over local governance docs) that returns **cited** answers
- **Eval harness** (JSONL + runner → pass-rate & P50 latency)
- **Dockerfile** for local container run
- **Terraform** stubs to demonstrate infra thinking
- **Governance** and **Enablement** docs

Quickstart:
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app/rag/ingest.py
uvicorn app.api:app --reload --port 8080
# http://127.0.0.1:8080/docs
```

Evaluate:
```bash
python evals/run.py
```


### Helpful docs
- `docs/demo_script_2min.md`
- `docs/case_study_template.md`


## Architecture
![AWS + Snowflake Reference](arch/reference_aws_snowflake.png)

## Demo (2-min)
Loom walkthrough: <link later>
