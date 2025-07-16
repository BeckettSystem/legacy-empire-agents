
from system.scrolls.scroll_base import ScrollBase
from system.utils.messaging import send_followup_text
from system.rituals.log import write_log_entry

class TextLoopScroll(ScrollBase):
    def execute(self, intent: dict):
        """
        Sends follow-up text message sequence based on lead lifecycle or event.
        """
        lead_id = intent.get("lead_id")
        message_type = intent.get("message_type", "check_in")
        tone = intent.get("tone", "friendly")

        result = send_followup_text(lead_id, message_type, tone)

        write_log_entry(agent="TextLoop", log_type="text_followup", data=result)

        return {
            "status": "sent",
            "result": result
        }
