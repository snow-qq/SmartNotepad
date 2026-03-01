from dataclasses import dataclass
from ui.tabs import TabManager
from editor.text_buffer import TextBuffer
from settings.user_settings import UserSettings
from settings.autosave import AutoSaveService


@dataclass
class MainWindow:
    settings: UserSettings
    autosave: AutoSaveService

    def __post_init__(self) -> None:
        self.tabs = TabManager()
        self.active_buffer = TextBuffer()

    def run(self) -> None:
        """
        Имитация запуска GUI.
        В реальном приложении здесь будет цикл событий (event loop) и отрисовка.
        """
        self.autosave.start()
        self.tabs.open_new_tab("Untitled", self.active_buffer)
        print("SmartNotepad запущен. Тема:", self.settings.theme_name)