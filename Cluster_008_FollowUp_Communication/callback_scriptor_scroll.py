
from system.scrolls.scroll_base import ScrollBase
from system.utils.dialogue import generate_callback_script
from system.rituals.log import write_log_entry

class CallbackScriptorScroll(ScrollBase):
    def execute(self, intent: dict):
        """
        Prepares callback scripts for voicemail or agent-led follow-up.
        """
        scenario = intent.get("scenario", "missed_call")
        client_profile = intent.get("client_profile", {})

        script = generate_callback_script(scenario, client_profile)

        write_log_entry(agent="CallbackScriptor", log_type="callback_script", data=script)

        return {
            "status": "prepared",
            "script": script
        }
