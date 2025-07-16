
from system.scrolls.scroll_base import ScrollBase
from system.utils.competitor_analysis import analyze_competitor_trends
from system.rituals.log import write_log_entry

class CompCurveScroll(ScrollBase):
    def execute(self, intent: dict):
        """
        Tracks and compares competitor strategies and offer trends.
        """
        market_data = intent.get("market_data", {})
        zip_code = intent.get("zip_code", "")

        trend_summary = analyze_competitor_trends(market_data, zip_code)

        write_log_entry(agent="CompCurve", log_type="comp_trend", data={
            "zip_code": zip_code,
            "trends": trend_summary
        })

        return {
            "status": "tracked",
            "trends": trend_summary
        }
