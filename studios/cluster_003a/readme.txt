# Beckett Studios: Cinematic Campaign AI Studio

## Quickstart

1. **Clone the repo / create the folder structure as described.**
2. **Paste the motif library into `/mastercraft_library/motifs.json`.**
3. **Add/expand agent folders in `/studios/` with:**
    - `soul.json`
    - `scroll.py`
    - `workflow.json`
    - `/logs/`, `/memory/` folders as needed
4. **Import `/n8n_workflows/studio_campaign_workflow.json` into your n8n instance.**
5. **Trigger campaigns by POSTing to the campaign webhook or through n8n UI.**

## Using Motifs

- Each campaign is based on a motif (see `/mastercraft_library/motifs.json`).
- Pick a motif or let the system suggest one based on your lead/client type.
- All agents (Apollo, Calliope, etc.) adapt their logic, script, and creative direction to the motif structure.
- Add new motifs by expanding the JSON file. The agents and workflows will reference new motifs automatically.

## Adding/Expanding Agents

- Each agent should include:
    - Persona-fused `soul.json`
    - Scroll-complete `scroll.py`
    - n8n-ready `workflow.json`
    - Logging/memory for tracking and legacy handoff

## Scale & Customization

- Use the motif library as your campaign template playbook.
- Add/modify motifs for new market segments, stories, or creative directions.
- Use as a template for other clusters (analytics, delivery, funnel, social, etc.).

## Support

- For workflow, agent, or motif issues, expand with new code or ask for best practices here!
