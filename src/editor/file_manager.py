from pathlib import Path
from typing import Optional


class FileManager:
    def open_text(self, path: str, encoding: str = "utf-8") -> str:
        return Path(path).read_text(encoding=encoding)

    def save_text(self, path: str, text: str, encoding: str = "utf-8") -> None:
        Path(path).write_text(text, encoding=encoding)

    def detect_extension(self, path: str) -> Optional[str]:
        p = Path(path)
        return p.suffix.lower() if p.suffix else None