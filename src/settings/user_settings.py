import json
from dataclasses import dataclass
from pathlib import Path


@dataclass
class UserSettings:
    theme_name: str = "light"
    autosave_interval_seconds: int = 60

    @staticmethod
    def load(path: str) -> "UserSettings":
        p = Path(path)
        if not p.exists():
            return UserSettings()
        data = json.loads(p.read_text(encoding="utf-8"))
        return UserSettings(
            theme_name=data.get("theme_name", "light"),
            autosave_interval_seconds=int(data.get("autosave_interval_seconds", 60)),
        )