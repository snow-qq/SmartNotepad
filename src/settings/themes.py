from dataclasses import dataclass


@dataclass(frozen=True)
class Theme:
    name: str
    background: str
    foreground: str


class ThemeManager:
    def __init__(self) -> None:
        self._themes = {
            "light": Theme("light", background="#FFFFFF", foreground="#333333"),
            "dark": Theme("dark", background="#111111", foreground="#EEEEEE"),
        }

    def get(self, name: str) -> Theme:
        return self._themes.get(name, self._themes["light"])

    def list_themes(self) -> list[str]:
        return list(self._themes.keys())