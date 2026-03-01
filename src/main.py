from ui.main_window import MainWindow
from settings.user_settings import UserSettings
from settings.autosave import AutoSaveService


def main() -> None:
    settings = UserSettings.load("config.json")
    autosave = AutoSaveService(interval_seconds=settings.autosave_interval_seconds)

    app = MainWindow(settings=settings, autosave=autosave)
    app.run()


if __name__ == "__main__":
    main()