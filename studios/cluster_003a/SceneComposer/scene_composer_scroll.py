
from system.scrolls.scroll_base import ScrollBase
from system.utils.storyboard import compose_scene_sequence
from system.rituals.log import write_log_entry

class SceneComposerScroll(ScrollBase):
    def execute(self, intent: dict):
        title = intent.get("title", "Untitled Storyboard")
        blocks = intent.get("scene_blocks", [])
        brand = intent.get("brand", "default")

        storyboard = compose_scene_sequence(blocks, brand)

        write_log_entry(agent="SceneComposer", log_type="storyboard_created", data={
            "title": title,
            "scenes": storyboard
        })

        return {
            "status": "composed",
            "storyboard": storyboard
        }
