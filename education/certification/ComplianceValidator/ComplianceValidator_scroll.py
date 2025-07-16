
"""
Scroll: ComplianceValidator
Purpose: Validate the legal and structural integrity of title-related data and ensure all documents align with regulatory and legacy safeguards.
"""

import re
import json

def validate_title_data(data):
    errors = []

    if "owner_name" not in data or not data["owner_name"]:
        errors.append("Missing owner name on record.")

    if "vesting_type" in data and data["vesting_type"] not in ["Joint Tenancy", "Tenancy in Common", "Sole Ownership"]:
        errors.append(f"Invalid vesting type: {data['vesting_type']}")

    if "document_text" in data:
        if "death certificate" in data["document_text"].lower() and "executor" not in data["document_text"].lower():
            errors.append("Potential probate oversight: death mentioned but no executor assigned.")

    return {"valid": len(errors) == 0, "issues": errors}
