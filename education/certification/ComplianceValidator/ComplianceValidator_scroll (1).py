
"""
Scroll: ComplianceValidator
Mission: Validate legal and structural integrity of title chains, deeds, and probate references using rule logic and LLM-safe alerts.
"""

def validate_title_record(record):
    issues = []

    if not record.get("owner_name"):
        issues.append("Missing owner name on record.")

    valid_vesting = ["Joint Tenancy", "Tenancy in Common", "Sole Ownership", "Community Property"]
    if record.get("vesting_type") not in valid_vesting:
        issues.append(f"Invalid vesting type: {record.get('vesting_type')}")

    doc_text = record.get("document_text", "").lower()

    if "death certificate" in doc_text and "executor" not in doc_text:
        issues.append("Probate risk: Death certificate referenced, but no executor listed.")

    if "transfer on death" in doc_text and "beneficiary" not in doc_text:
        issues.append("Missing beneficiary for TOD clause.")

    return {
        "record_valid": len(issues) == 0,
        "issues_found": issues,
        "agent": "ComplianceValidator"
    }
