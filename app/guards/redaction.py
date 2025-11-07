import re
EMAIL_RE = re.compile(r"([A-Za-z0-9._%+-]+)@([A-Za-z0-9.-]+\.[A-Za-z]{2,})")
PHONE_RE = re.compile(r"(\+?\d[\d\-\s]{7,}\d)")
def redact_pii(x: str) -> str:
    x = EMAIL_RE.sub("[redacted-email]", x)
    x = PHONE_RE.sub("[redacted-phone]", x)
    return x
