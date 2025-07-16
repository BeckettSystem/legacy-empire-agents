
from system.scrolls.scroll_base import ScrollBase
from system.utils.reactivation import attempt_lead_reactivation
from system.rituals.log import write_log_entry

class ReigniteBotScroll(ScrollBase):
    def execute(self, intent: dict):
        """
        Attempts to resurrect cold leads with personalized reactivation strategy.
        """
        lead_id = intent.get("lead_id")
        cold_duration = intent.get("cold_days", 30)

        result = attempt_lead_reactivation(lead_id, cold_duration)

        write_log_entry(agent="ReigniteBot", log_type="reactivation_attempt", data={
            "lead_id": lead_id,
            "cold_duration": cold_duration,
            "result": result
        })

        return {
            "status": "reactivation_attempted",
            "result": result
        }
