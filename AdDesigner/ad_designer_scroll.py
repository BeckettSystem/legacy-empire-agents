
from system.scrolls.scroll_base import ScrollBase
from system.utils.ad_builder import create_ad_concept
from system.rituals.log import write_log_entry

class AdDesignerScroll(ScrollBase):
    def execute(self, intent: dict):
        """
        Designs paid or organic ad concepts based on audience and format.
        """
        campaign_name = intent.get("campaign_name", "")
        audience_segment = intent.get("audience", "general")
        format_type = intent.get("format", "carousel")

        ad_concept = create_ad_concept(campaign_name, audience_segment, format_type)

        write_log_entry(agent="AdDesigner", log_type="ad_concept", data=ad_concept)

        return {
            "status": "ad_ready",
            "ad_concept": ad_concept
        }
