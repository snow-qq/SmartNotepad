from dataclasses import dataclass


@dataclass
class TextBuffer:
    text: str = ""
    is_dirty: bool = False

    def insert(self, content: str) -> None:
        self.text += content
        self.is_dirty = True

    def replace(self, new_text: str) -> None:
        self.text = new_text
        self.is_dirty = True

    def clear(self) -> None:
        self.text = ""
        self.is_dirty = True