
from system.scrolls.scroll_base import ScrollBase
from system.utils.touchpoints import schedule_check_in
from system.rituals.log import write_log_entry

class CheckInBotScroll(ScrollBase):
    def execute(self, intent: dict):
        """
        Schedules or sends a periodic check-in to maintain lead warmth.
        """
        lead_id = intent.get("lead_id")
        interval = intent.get("interval_days", 7)
        channel = intent.get("channel", "sms")

        result = schedule_check_in(lead_id, interval, channel)

        write_log_entry(agent="CheckInBot", log_type="check_in", data=result)

        return {
            "status": "check_in_scheduled",
            "result": result
        }
