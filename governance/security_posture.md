# Security Posture (Demo)
- Read-only data roles (RBAC), no wildcards
- No secrets in code; rotate & store in manager
- Private endpoints; restrict inbound/egress
- Structured logs; redact PII
- **Encryption:** TLS in transit; AES-256 at rest.
- **Latency Goal:** Target P50 latency under 1s for common queries.

