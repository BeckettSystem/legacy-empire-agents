
"""
Scroll: DrillForge
Purpose: Generate agent drills, scroll flashcards, and recall tests from longform scrolls, documentation, or transcripts.
"""

def generate_flashcards(content):
    cards = []
    lines = content.split("\n")
    for line in lines:
        if ":" in line:
            key, value = line.split(":", 1)
            question = f"What is the definition of {key.strip()}?"
            answer = value.strip()
            cards.append({"question": question, "answer": answer})
    return cards
