
"""
Scroll: ScrollBadgeBinder
Purpose: Assign achievement badges or status seals based on agent performance, scroll completions, or legal case interactions.
"""

def assign_badges(agent_activity_log):
    badges = []

    if agent_activity_log.get("certified_scrolls", 0) >= 10:
        badges.append("Scroll Mastery Level 1")

    if agent_activity_log.get("compliance_flags", 0) == 0 and agent_activity_log.get("actions_reviewed", 0) >= 20:
        badges.append("Integrity Seal")

    if "title_cleared" in agent_activity_log.get("milestones", []):
        badges.append("Chainbreaker Badge")

    return badges
