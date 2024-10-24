import os

from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.screen import Screen
from textual.widgets import DirectoryTree, TextArea

from pyide.widgets import CodeArea, FileTree


class EditorScreen(Screen):
    def __init__(self) -> None:
        super().__init__()
        self._file_tree = FileTree(os.path.curdir)
        self._text_area = TextArea()

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield self._file_tree
            yield self._text_area

    async def on_directory_tree_file_selected(self, event: DirectoryTree.FileSelected):
        self.notify(str(event.path))
        self._text_area = CodeArea(event.path)
        await self.recompose()
