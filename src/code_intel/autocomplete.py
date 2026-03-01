from dataclasses import dataclass


@dataclass
class Suggestion:
    value: str
    kind: str


class AutoCompleteEngine:
    """
    Имитация автодополнения: выдаёт подсказки по префиксу.
    """

    def __init__(self) -> None:
        self._words = [
            "def", "class", "return", "import", "from", "for", "while",
            "try", "except", "finally", "with", "yield"
        ]

    def suggest(self, prefix: str) -> list[Suggestion]:
        p = prefix.strip()
        if not p:
            return []
        return [Suggestion(w, "keyword") for w in self._words if w.startswith(p)]