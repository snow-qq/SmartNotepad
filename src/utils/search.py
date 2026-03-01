import re


class SearchService:
    def find_all(self, text: str, query: str, case_sensitive: bool = False) -> list[tuple[int, int]]:
        flags = 0 if case_sensitive else re.IGNORECASE
        pattern = re.compile(re.escape(query), flags)
        return [(m.start(), m.end()) for m in pattern.finditer(text)]