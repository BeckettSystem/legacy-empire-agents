
from system.scrolls.scroll_base import ScrollBase
from system.utils.sentiment import detect_engagement_drift
from system.rituals.log import write_log_entry

class DriftTrackerScroll(ScrollBase):
    def execute(self, intent: dict):
        """
        Monitors sentiment shift and engagement decay over time.
        """
        lead_id = intent.get("lead_id")
        interaction_log = intent.get("interaction_log", [])

        drift_score = detect_engagement_drift(interaction_log)

        write_log_entry(agent="DriftTracker", log_type="sentiment_drift", data={
            "lead_id": lead_id,
            "drift_score": drift_score
        })

        return {
            "status": "tracked",
            "drift_score": drift_score
        }
