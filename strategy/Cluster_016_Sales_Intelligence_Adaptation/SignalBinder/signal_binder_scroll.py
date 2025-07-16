
from system.scrolls.scroll_base import ScrollBase
from system.utils.signal_integration import bind_external_signals
from system.rituals.log import write_log_entry

class SignalBinderScroll(ScrollBase):
    def execute(self, intent: dict):
        """
        Integrates and scores signals from external platforms (Zillow, Redfin, MLS, etc.).
        """
        external_signals = intent.get("external_signals", [])
        source = intent.get("source", "unspecified")

        bound_result = bind_external_signals(external_signals, source)

        write_log_entry(agent="SignalBinder", log_type="signal_input", data={
            "source": source,
            "signals": external_signals,
            "result": bound_result
        })

        return {
            "status": "bound",
            "result": bound_result
        }
