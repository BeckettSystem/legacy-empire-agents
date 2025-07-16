
from datetime import datetime
from system.scrolls.scroll_base import ScrollBase
from system.utils.dispatcher import dispatch_campaign_trigger
from system.rituals.log import log_campaign_rhythm

class ApolloScroll(ScrollBase):
    def execute(self, intent: dict):
        campaign_name = intent.get("campaign_name", "Unnamed Campaign")
        target_audience = intent.get("target_audience", "General")
        launch_sequence = intent.get("launch_sequence", [])
        timing = intent.get("timing", "immediate")

        log_campaign_rhythm(agent="Apollo", campaign=campaign_name, timestamp=str(datetime.utcnow()))

        for step in launch_sequence:
            dispatch_campaign_trigger(
                agent=step.get("agent"),
                scroll=step.get("scroll"),
                audience=target_audience,
                mode=timing
            )

        return {
            "status": "launched",
            "campaign": campaign_name
        }
