from textual.app import App

from pyide.screens import EditorScreen


class PyIDE(App):
    ENABLE_COMMAND_PALETTE = False
    CSS_PATH = "style.tcss"

    def on_mount(self):
        self.push_screen(EditorScreen())
