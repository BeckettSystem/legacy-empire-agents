
from system.scrolls.scroll_base import ScrollBase
from system.utils.geo_tracker import analyze_geo_activity
from system.rituals.log import write_log_entry

class GeoFocusScroll(ScrollBase):
    def execute(self, intent: dict):
        """
        Evaluates specific area or zip code activity and sales trends.
        """
        area_code = intent.get("area_code", "")
        activity_data = intent.get("activity_data", {})

        geo_result = analyze_geo_activity(area_code, activity_data)

        write_log_entry(agent="GeoFocus", log_type="geo_activity", data={
            "area_code": area_code,
            "summary": geo_result
        })

        return {
            "status": "geo_evaluated",
            "summary": geo_result
        }
