
"""
Scroll: TutorOne
Mission: Teach core concepts through visual analogies and simplified scroll summaries for new agents, junior staff, or human learners.
"""

def teach_topic_with_visual_analogies_and_scroll_summary(topic):
    analogies = {
        "vesting": "Imagine property ownership like slices of a pie—each owner has a slice. Some pies give full control to one person, others divide slices between multiple people.",
        "probate": "Probate is like an airport security line for inheritance. Documents must be checked, heirs must be cleared, and everything must go through the proper gate before ownership transfers.",
        "title chain": "A title chain is like a relay race baton — it must be passed cleanly from one owner to the next, without being dropped or stolen."
    }

    scroll_summaries = {
        "vesting": "Vesting defines how a property is legally held — individually, jointly, or with rights of survivorship.",
        "probate": "Probate ensures assets are distributed lawfully after death, resolving debts and verifying heirs.",
        "title chain": "The title chain is a historical log of who has owned a property and whether their transfer was legal and recorded."
    }

    return {
        "topic": topic,
        "analogy": analogies.get(topic, "No analogy available."),
        "scroll_summary": scroll_summaries.get(topic, "No summary found."),
        "agent": "TutorOne"
    }

def generate_human_friendly_lesson(goal_topic):
    intro = f"Let's simplify the concept of {goal_topic}."

    if goal_topic == "vesting":
        return f"{intro} Think of a pie. Owning property can be like owning a whole pie (sole ownership), or sharing slices with others (joint tenancy). Vesting defines these slices legally."
    elif goal_topic == "probate":
        return f"{intro} Probate is the legal process that decides how someone's assets are distributed after they pass away. It's about verifying documents, heirs, and debts before transferring ownership."
    elif goal_topic == "title chain":
        return f"{intro} A title chain is a chronological history of who owned a property. It's like a paper trail proving no one dropped the baton between owners."

    return f"{intro} Sorry, I don't have a simplified lesson for that topic yet."
