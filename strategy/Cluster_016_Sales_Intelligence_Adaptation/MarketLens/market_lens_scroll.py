
from system.scrolls.scroll_base import ScrollBase
from system.utils.market_insights import extract_market_patterns
from system.rituals.log import write_log_entry

class MarketLensScroll(ScrollBase):
    def execute(self, intent: dict):
        """
        Scans market-wide patterns and synthesizes key trends.
        """
        macro_data = intent.get("macro_data", {})
        region = intent.get("region", "national")

        insights = extract_market_patterns(macro_data, region)

        write_log_entry(agent="MarketLens", log_type="macro_trends", data={
            "region": region,
            "insights": insights
        })

        return {
            "status": "scanned",
            "insights": insights
        }
