
from .scroll import scroll
from ga_notice_scraper import scrape_ga_public_notices
from signal_categorizer import categorize_notice
from skip_trace_handler import trace_decision_maker
from lead_score_engine import score_lead
from falcon_flag_dispatch import dispatch_lead_to_allies
from datetime import datetime

class Falcon:
    def __init__(self):
        self.profile = scroll()

    def run_signal_sweep(self, keywords=None):
        notices = scrape_ga_public_notices(keywords=keywords)
        reports = []

        for notice in notices:
            category = categorize_notice(notice)
            contact = trace_decision_maker(notice['name'], notice['address'])
            score = score_lead(notice, contact)
            dispatch = dispatch_lead_to_allies(notice, contact, score)

            reports.append({
                "category": category,
                "notice": notice,
                "contact": contact,
                "score": score,
                "dispatch": dispatch
            })

        return {
            "report": reports,
            "timestamp": datetime.utcnow().isoformat()
        }
