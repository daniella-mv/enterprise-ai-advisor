# 2-Minute Demo Script — Enterprise AI Advisor
**Goal:** Show architecture thinking, governance, and evals in under 120 seconds.

**0:00–0:15 — Problem & Audience**
- “This advisor helps analysts and leaders get *cited* answers across policy/case notes, with governance built-in.”

**0:15–0:40 — Architecture at a glance**
- “Local demo here; production uses **AWS + Snowflake + Bedrock**. VPC → private Snowflake → LLM API → API surface → logs.”
- “RBAC read-only role, no secrets in code, audit logs. Diagram in `arch/`.”

**0:40–1:10 — Live flow**
1. Open `http://127.0.0.1:8080/docs` → **/ask**.
2. Ask: “What are our rules for PII?”
3. Show answer with **citations**; highlight **PII redaction** and **strict JSON** option.

**1:10–1:35 — Evals & reliability**
- “I gate changes with an **eval harness**. Let me run it.”  
  `python evals/run.py` → “Pass-rate, P50 latency saved to CSV.”  
- “Any regression fails CI; we roll back.”

**1:35–1:55 — Security & enablement**
- “Responsible AI checklist & security posture are versioned in `governance/`.”
- “I also bring a **4-session enablement plan** so internal teams can own this.”

**1:55–2:00 — Close**
- “Happy to discuss how this maps to FedRAMP/IAM controls and an EKS/ECS deploy.”
