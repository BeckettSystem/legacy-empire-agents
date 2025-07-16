
from system.scrolls.scroll_base import ScrollBase
from system.utils.flyer_generator import create_listing_flyer
from system.rituals.log import write_log_entry

class FlyerBuilderScroll(ScrollBase):
    def execute(self, intent: dict):
        """
        Generates property flyers, listing packets, and print-ready assets.
        """
        listing_data = intent.get("listing", {})
        design_style = intent.get("style", "clean")

        flyer = create_listing_flyer(listing_data, design_style)

        write_log_entry(agent="FlyerBuilder", log_type="flyer_generated", data=flyer)

        return {
            "status": "flyer_built",
            "flyer": flyer
        }
