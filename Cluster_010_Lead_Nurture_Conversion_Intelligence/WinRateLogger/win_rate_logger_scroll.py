
from system.scrolls.scroll_base import ScrollBase
from system.rituals.log import write_log_entry
from system.utils.analytics import evaluate_win_rate

class WinRateLoggerScroll(ScrollBase):
    def execute(self, intent: dict):
        """
        Logs outcome of lead interaction and updates win/loss analytics.
        """
        lead_id = intent.get("lead_id")
        result = intent.get("result", "unknown")
        notes = intent.get("notes", "")

        win_rate = evaluate_win_rate(lead_id, result)

        write_log_entry(agent="WinRateLogger", log_type="conversion_result", data={
            "lead_id": lead_id,
            "result": result,
            "notes": notes,
            "win_rate": win_rate
        })

        return {
            "status": "logged",
            "win_rate": win_rate
        }
