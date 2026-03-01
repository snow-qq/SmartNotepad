import re
from dataclasses import dataclass
from typing import Dict, Pattern


@dataclass
class HighlightRule:
    name: str
    pattern: Pattern[str]


class SyntaxHighlighter:
    """
    Имитация синтаксической подсветки: выдаёт позиции токенов по правилам.
    """

    def __init__(self) -> None:
        self._rules: Dict[str, list[HighlightRule]] = {}

    def register_language(self, lang: str, rules: list[HighlightRule]) -> None:
        self._rules[lang.lower()] = rules

    def tokenize(self, lang: str, text: str) -> list[dict]:
        rules = self._rules.get(lang.lower(), [])
        tokens: list[dict] = []
        for rule in rules:
            for m in rule.pattern.finditer(text):
                tokens.append(
                    {"type": rule.name, "start": m.start(), "end": m.end(), "value": m.group(0)}
                )
        tokens.sort(key=lambda t: (t["start"], t["end"]))
        return tokens


def default_python_rules() -> list[HighlightRule]:
    kw = r"\b(False|True|None|and|as|assert|async|await|break|class|continue|def|del|elif|else|except|finally|for|from|global|if|import|in|is|lambda|nonlocal|not|or|pass|raise|return|try|while|with|yield)\b"
    return [
        HighlightRule("keyword", re.compile(kw)),
        HighlightRule("comment", re.compile(r"#.*")),
        HighlightRule("string", re.compile(r"(\"\"\".*?\"\"\"|\'\'\'.*?\'\'\'|\".*?\"|\'.*?\')", re.DOTALL)),
        HighlightRule("number", re.compile(r"\b\d+(\.\d+)?\b")),
    ]