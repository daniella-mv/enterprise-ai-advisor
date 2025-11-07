# Case Study — Secure RAG Advisor (Template)

## 1) Context
- **Agency/Domain:** e.g., fraud/waste/abuse triage
- **Stakeholders:** Investigators, policy owners, data platform team
- **Constraints:** FedRAMP boundary, RBAC/PII controls, auditability, limited headcount

## 2) Problem → Why now
- Analysts spend X hrs/week searching docs; answers are inconsistent; risk of exposing PII in responses.
- Leaders want measurable improvements in **time-to-answer** and **error rate** (hallucinations).

## 3) Solution (What we built)
- **Architecture:** AWS VPC, private Snowflake access, LLM API (Bedrock/Vertex/Azure), API surface (FastAPI), containerized runtime.
- **RAG:** Chunked policy corpus with **cited** answers; strict JSON mode for structured outputs.
- **Governance:** PII redaction, prompt-injection testing, audit logs, least-privilege RBAC.

## 4) Outcomes (Metrics)
- **Pass-rate:** __% across __ eval cases (policy/PII/injection/RBAC)
- **P50 latency:** __ s   |   **P95 latency:** __ s
- **Coverage:** __% of common policy questions answered with citations
- **Safety:** 0 critical PII leaks in evals

## 5) Rollout & Enablement
- 4-session plan: Use-case → Access/RBAC → Build-along → Operate (evals CI, rollback, docs)
- Handover artifacts: architecture diagram, runbooks, eval suite, governance docs

## 6) Next steps
- Productionize: EKS/ECS + secrets mgr + observability
- Extend evals to __ cases; add cost/latency budgets
- Integrate Snowflake vector search or managed vector DB


* Pass-rate: 100% across 3 eval cases
* P50 latency: 0.0 s
* Coverage: start with policy/PII basics
* Safety: 0 critical PII leaks in current evals


Pass-rate: 93.3% across 15 eval cases

P50 latency: 0.0 s (toy corpus)

Coverage: policy/PII/injection/RBAC basics with citations

Safety: 0 critical PII leaks in evals

