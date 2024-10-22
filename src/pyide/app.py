from textual.app import App, ComposeResult
from textual.widgets import Static


class PyIDE(App):
    def compose(self) -> ComposeResult:
        yield Static("PyIDE")
