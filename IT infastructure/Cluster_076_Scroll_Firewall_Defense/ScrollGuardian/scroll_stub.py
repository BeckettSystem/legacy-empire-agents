import re
from system.scrolls.utils import send_alert, log_event

ALLOWED_SCROLLS = ["valid_scroll_id_1", "valid_scroll_id_2"]  # replaced during runtime from scroll_registry.json

def sanitize_payload(payload):
    suspicious = re.search(r"(;|<script|DROP TABLE|--|eval\(|\\x00)", str(payload), re.IGNORECASE)
    return suspicious is None

def run(scroll_id, payload):
    log_event("firewall_activity_log.json", f"Incoming scroll: {scroll_id}")

    if scroll_id not in ALLOWED_SCROLLS:
        send_alert("Valor", f"Unauthorized scroll attempt: {scroll_id}")
        log_event("quarantine_log.json", {"scroll_id": scroll_id, "reason": "Not whitelisted"})
        return {"status": "blocked", "reason": "unauthorized_scroll"}

    if not sanitize_payload(payload):
        send_alert("Cipher", f"Suspicious payload detected in scroll {scroll_id}")
        log_event("suspicion_scores.json", {"scroll_id": scroll_id, "score": 98})
        log_event("quarantine_log.json", {"scroll_id": scroll_id, "reason": "Payload sanitization failed"})
        return {"status": "blocked", "reason": "payload_malicious"}

    return {"status": "allowed"}