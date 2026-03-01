class SemanticAnalyzer:
    """
    Имитация семантического анализа: проверка парных скобок и кавычек.
    """

    def check_pairs(self, text: str) -> list[str]:
        errors: list[str] = []
        if text.count("(") != text.count(")"):
            errors.append("Несбалансированные круглые скобки.")
        if text.count("{") != text.count("}"):
            errors.append("Несбалансированные фигурные скобки.")
        if text.count("[") != text.count("]"):
            errors.append("Несбалансированные квадратные скобки.")
        if text.count("\"") % 2 != 0:
            errors.append("Не закрыта двойная кавычка.")
        if text.count("'") % 2 != 0:
            errors.append("Не закрыта одинарная кавычка.")
        return errors