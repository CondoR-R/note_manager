import pathlib

from .models import manager
from .tui import app


def main():
    path = pathlib.Path(__file__).parent.parent / "notes.json"
    n = manager.NoteManager(filepath=path)
    app.run(n)


if __name__ == "__main__":
    main()
