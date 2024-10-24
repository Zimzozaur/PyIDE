from pathlib import Path

from textual.widgets import TextArea

extensions_to_languages = {
    ".go": "go",
    ".java": "java",
    ".js": "javascript",
    ".mjs": "javascript",
    ".kt": "kotlin",
    ".kts": "kotlin",
    ".py": "python",
    ".rs": "rust",
}


class CodeArea(TextArea):
    def __init__(self, code_path: Path) -> None:
        text = "".join(open(code_path))  # noqa: PTH123, SIM115
        lang = extensions_to_languages.get(code_path.suffix)
        super().__init__(
            text,
            language=lang,
            tab_behavior="indent",
            show_line_numbers=True,
        )
