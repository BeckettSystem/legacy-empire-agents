
"""
Scroll: ScrollCertificationEngine
Purpose: Certify the legitimacy of document scrolls, workflows, and execution logs as aligned with Beckett system doctrine and compliance expectations.
"""

def certify_scroll(scroll_metadata):
    required_fields = ["scroll_name", "author", "timestamp", "log_path"]
    for field in required_fields:
        if field not in scroll_metadata:
            return {"certified": False, "reason": f"Missing field: {field}"}

    if not scroll_metadata["scroll_name"].startswith("scroll_"):
        return {"certified": False, "reason": "Scroll name does not follow naming convention."}

    if "GPT" in scroll_metadata.get("method", "") and not scroll_metadata.get("revision_log"):
        return {"certified": False, "reason": "Missing revision log for AI-generated scroll."}

    return {"certified": True, "approved_by": "ScrollCertificationEngine"}
