
"""
Scroll: ScrollCertificationEngine
Mission: Certify the authenticity, structure, and revision integrity of scrolls before archive submission or execution.
"""

def certify_scroll_package(metadata):
    required_keys = ["scroll_id", "author", "last_modified", "log_path", "version"]
    for key in required_keys:
        if key not in metadata:
            return {
                "certified": False,
                "reason": f"Missing required metadata: {key}"
            }

    if not metadata["scroll_id"].startswith("scroll_"):
        return {
            "certified": False,
            "reason": "Scroll ID must start with 'scroll_' prefix"
        }

    if "AI" in metadata.get("origin", "") and not metadata.get("revision_log"):
        return {
            "certified": False,
            "reason": "Missing revision trail for AI-generated scroll"
        }

    return {
        "certified": True,
        "certified_by": "ScrollCertificationEngine",
        "scroll_id": metadata["scroll_id"]
    }
