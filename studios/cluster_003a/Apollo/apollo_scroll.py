import json

def load_motif(motif_path):
    with open(motif_path, 'r') as f:
        motifs = json.load(f)["motifs"]
    return motifs

def pre_campaign_brief(brief, motif_name, motif_path="./mastercraft_library/motifs.json"):
    motifs = load_motif(motif_path)
    motif = next((m for m in motifs if m["name"] == motif_name), motifs[0])
    print(f"Selected motif: {motif['name']}")
    campaign_brief = {
        "motif": motif['name'],
        "visuals": motif['visuals'],
        "audio": motif['audio'],
        "story_arc": motif['story_arc'],
        "cta": motif['cta'],
        "platforms": motif['platforms'],
        "user_brief": brief
    }
    return campaign_brief

def orchestrate_campaign(brief, motif_name="Bond in Atlanta"):
    campaign_brief = pre_campaign_brief(brief, motif_name)
    print("Apollo is assembling the team and vision...")
    # handoff to Calliope, Ritchie, etc.
    return campaign_brief

# Example usage:
if __name__ == "__main__":
    user_brief = "30s cinematic YouTube ad for a luxury listing in Atlanta"
    result = orchestrate_campaign(user_brief, "Bond in Atlanta")
    print(json.dumps(result, indent=2))
