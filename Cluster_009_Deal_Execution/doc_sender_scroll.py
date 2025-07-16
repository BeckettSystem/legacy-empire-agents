
from system.scrolls.scroll_base import ScrollBase
from system.utils.delivery import send_document_package
from system.rituals.log import write_log_entry

class DocSenderScroll(ScrollBase):
    def execute(self, intent: dict):
        document_bundle = intent.get("bundle", {})
        recipient = intent.get("recipient", "")
        delivery_method = intent.get("method", "email")

        result = send_document_package(document_bundle, recipient, delivery_method)

        write_log_entry(agent="DocSender", log_type="document_delivery", data=result)

        return {
            "status": "sent",
            "result": result
        }
