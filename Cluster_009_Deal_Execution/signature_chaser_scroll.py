
from system.scrolls.scroll_base import ScrollBase
from system.utils.signatures import track_pending_signatures
from system.rituals.log import write_log_entry

class SignatureChaserScroll(ScrollBase):
    def execute(self, intent: dict):
        envelope_id = intent.get("envelope_id", "")
        parties = intent.get("signers", [])

        status = track_pending_signatures(envelope_id, parties)

        write_log_entry(agent="SignatureChaser", log_type="signature_status", data={
            "envelope_id": envelope_id,
            "status": status
        })

        return {
            "status": "tracked",
            "signature_status": status
        }
