
from system.scrolls.scroll_base import ScrollBase
from system.utils.persona import update_persona_profile
from system.rituals.log import write_log_entry

class PersonaProfilerScroll(ScrollBase):
    def execute(self, intent: dict):
        """
        Updates lead persona based on tone, response, or form inputs.
        """
        lead_id = intent.get("lead_id")
        new_inputs = intent.get("inputs", {})

        persona = update_persona_profile(lead_id, new_inputs)

        write_log_entry(agent="PersonaProfiler", log_type="persona_update", data={
            "lead_id": lead_id,
            "persona": persona
        })

        return {
            "status": "profile_updated",
            "persona": persona
        }
