
from datetime import datetime
from system.scrolls.scroll_base import ScrollBase
from system.rituals.log import write_log_entry
from system.utils.notify import notify_if_milestone_reached

class ClientChronicleScroll(ScrollBase):
    def execute(self, intent: dict):
        """
        Logs a lead’s activity and tracks engagement timeline.
        Used post-email, SMS, form fill, site click, etc.
        """
        lead_id = intent.get("lead_id")
        event_type = intent.get("event_type", "unspecified_event")
        details = intent.get("details", {})
        timestamp = intent.get("timestamp", datetime.utcnow().isoformat())

        log_data = {
            "lead_id": lead_id,
            "event_type": event_type,
            "details": details,
            "timestamp": timestamp
        }

        # Write engagement event to the log
        write_log_entry(agent="ClientChronicle", log_type="engagement", data=log_data)

        # Optional: milestone detection (e.g., 3rd click, 2nd reply, form submit)
        notify_if_milestone_reached(lead_id, event_type)

        return {
            "status": "logged",
            "lead_id": lead_id,
            "event": event_type,
            "timestamp": timestamp
        }
