
"""
Scroll: CoreCurriculum
Purpose: Generate and update role-based learning tracks for internal agents based on cluster assignments and evolution status.
"""

def generate_learning_path(agent_profile):
    track = []

    if agent_profile["cluster"] == "cluster_132_scrollcert":
        track = [
            "Intro to Title Law",
            "Probate Chain Defense",
            "Scroll Ethics & Legacy Protection",
            "Vesting Dispute Resolution"
        ]
    elif agent_profile["cluster"] == "cluster_126_scholar_core":
        track = [
            "Scroll Construction 101",
            "Agent Soul Design",
            "Curriculum Mapping for Cluster Training"
        ]

    if agent_profile.get("status") == "Legacy":
        track.append("Scroll Resurrection & Reinforcement")

    return track
