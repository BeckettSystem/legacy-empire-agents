
from system.scrolls.scroll_base import ScrollBase
from system.utils.move_patterns import detect_move_trends
from system.rituals.log import write_log_entry

class MoveWatcherScroll(ScrollBase):
    def execute(self, intent: dict):
        """
        Tracks buyer/seller relocations and regional hot/cold migration patterns.
        """
        movement_data = intent.get("movement_data", {})

        trend_analysis = detect_move_trends(movement_data)

        write_log_entry(agent="MoveWatcher", log_type="move_patterns", data=trend_analysis)

        return {
            "status": "movement_tracked",
            "patterns": trend_analysis
        }
