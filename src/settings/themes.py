from dataclasses import dataclass


@dataclass(frozen=True)
class Theme:
    name: str
    background: str
    foreground: str

    """
    Класс ThemeManager предназначен для управления темами оформления
    текстового редактора SmartNotepad.

    Данный класс хранит доступные темы интерфейса и позволяет
    переключать их во время работы программы.

    Attributes:
        themes (dict): список доступных тем оформления.
    """
class ThemeManager:
    """Создает набор стандартных тем оформления."""
    def __init__(self) -> None:
        self._themes = {
            "light": Theme("light", background="#FFFFFF", foreground="#111111"),
            "dark": Theme("dark", background="#111111", foreground="#EEEEEE"),
        }

    def get(self, name: str) -> Theme:
        """
        Возвращает параметры выбранной темы оформления.

         Args:
            name (str): название темы оформления.

        Returns:
            dict: параметры цветовой схемы интерфейса.
        """
        return self._themes.get(name, self._themes["light"])

    def list_themes(self) -> list[str]:
        return list(self._themes.keys())