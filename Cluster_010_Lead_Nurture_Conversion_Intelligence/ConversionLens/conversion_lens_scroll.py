
from system.scrolls.scroll_base import ScrollBase
from system.utils.cta_analyzer import analyze_cta_effectiveness
from system.rituals.log import write_log_entry

class ConversionLensScroll(ScrollBase):
    def execute(self, intent: dict):
        """
        Analyzes call-to-action performance and detects conversion friction.
        """
        cta_text = intent.get("cta_text", "")
        page_url = intent.get("page_url", "")
        click_data = intent.get("click_data", {})
        audience_segment = intent.get("audience_segment", "general")

        analysis = analyze_cta_effectiveness(cta_text, click_data, audience_segment)

        write_log_entry(agent="ConversionLens", log_type="cta_analysis", data={
            "cta_text": cta_text,
            "url": page_url,
            "analysis": analysis
        })

        return {
            "status": "analyzed",
            "cta": cta_text,
            "analysis": analysis
        }
