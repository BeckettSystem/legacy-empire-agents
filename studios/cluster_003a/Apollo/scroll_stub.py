# Scroll Rituals for Apollo

def pre_task_ritual(mode="default"):
    if mode == "compose":
        return "Engage story alignment. Prepare tone and visual arc."
    elif mode == "render":
        return "Prepare asset formatting. Begin final delivery pass."
    elif mode == "audio":
        return "Engage voice refinement. Sync narration elements."
    return "Activate primary directive."

def post_task_reflection(result):
    if "feedback" in result:
        return "Log feedback. Reflect with Echo and Pulse. Sync scroll memory."
    return "Archive output. Confirm ritual and dream log."
