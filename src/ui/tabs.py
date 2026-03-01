from dataclasses import dataclass
from typing import Dict
from editor.text_buffer import TextBuffer


@dataclass
class TabManager:
    def __post_init__(self) -> None:
        self._tabs: Dict[str, TextBuffer] = {}

    def open_new_tab(self, title: str, buffer: TextBuffer) -> None:
        self._tabs[title] = buffer

    def close_tab(self, title: str) -> None:
        self._tabs.pop(title, None)

    def list_tabs(self) -> list[str]:
        return list(self._tabs.keys())