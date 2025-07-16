
from system.scrolls.scroll_base import ScrollBase
from system.utils.outreach import send_nurture_sequence
from system.rituals.log import write_log_entry

class NurtureEngineScroll(ScrollBase):
    def execute(self, intent: dict):
        """
        Sends scheduled nurture sequence based on lead lifecycle.
        """
        lead_id = intent.get("lead_id")
        sequence_type = intent.get("sequence_type", "default")
        delivery_channel = intent.get("channel", "email")

        result = send_nurture_sequence(lead_id, sequence_type, delivery_channel)

        write_log_entry(agent="NurtureEngine", log_type="nurture_dispatch", data={
            "lead_id": lead_id,
            "sequence": sequence_type,
            "channel": delivery_channel,
            "status": result
        })

        return {
            "status": "dispatched",
            "result": result
        }
