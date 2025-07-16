
from system.scrolls.scroll_base import ScrollBase
from system.utils.visual_strategy import generate_visual_brief
from system.rituals.log import write_log_entry

class CreativeCuratorScroll(ScrollBase):
    def execute(self, intent: dict):
        """
        Generates visual direction briefs for design agents and content creators.
        """
        campaign_goal = intent.get("goal", "brand awareness")
        platform = intent.get("platform", "Instagram")
        brand_style = intent.get("style", "modern luxe")

        brief = generate_visual_brief(campaign_goal, platform, brand_style)

        write_log_entry(agent="CreativeCurator", log_type="visual_brief", data=brief)

        return {
            "status": "brief_generated",
            "brief": brief
        }
