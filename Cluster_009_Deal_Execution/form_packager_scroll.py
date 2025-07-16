
from system.scrolls.scroll_base import ScrollBase
from system.utils.docs import generate_offer_form_package
from system.rituals.log import write_log_entry

class FormPackagerScroll(ScrollBase):
    def execute(self, intent: dict):
        deal_data = intent.get("deal_data", {})
        template_type = intent.get("template", "standard")

        packet = generate_offer_form_package(deal_data, template_type)

        write_log_entry(agent="FormPackager", log_type="form_packet_created", data=packet)

        return {
            "status": "packet_created",
            "packet": packet
        }
