import json
import pathlib
import sys

from note_manager import constants, utils
from note_manager.models import note


class NoteManager:
    def __init__(self, filepath: pathlib.Path):
        self._filepath = filepath
        self._notes: list[note.Note]

    def _load(self):
        """
        Загрузка и парсинг данных из JSON файла.
        Преобразование словарей в note.Note.
        """
        self._notes = []

        if not self._filepath.exists():
            return

        with open(self._filepath, "r", encoding="utf-8") as file:
            try:
                json_notes = json.load(file)
                for json_note in json_notes:
                    n = note.Note(
                        id=json_note["id"],
                        title=json_note["title"],
                        content=json_note["content"],
                        tags=json_note.get("tags", []),
                        created_at=utils.str_to_datetime(json_note["created_at"]),
                        updated_at=utils.str_to_datetime(json_note["updated_at"]),
                    )
                    self._notes.append(n)
            except json.JSONDecodeError as err:
                print(f"Ошибка: {err}", file=sys.stderr)
                # создаем резервную копию
                backup_path = self._filepath.with_name(self._filepath.name + ".bak")
                self._filepath.replace(backup_path)

    def _save(self):
        """
        Сохранение данных в JSON файл (с конвертацией дат в строки).
        """
        tmp_path = self._filepath.with_name(self._filepath.name + ".tmp")
        with open(
            tmp_path,
            "w",
            encoding="utf-8",
        ) as file:
            notes = []
            for n in self._notes:
                notes.append(
                    {
                        "id": n.id,
                        "title": n.title,
                        "content": n.content,
                        "tags": n.tags,
                        "created_at": utils.datetime_to_str(n.created_at),
                        "updated_at": utils.datetime_to_str(n.updated_at),
                    }
                )
            json.dump(notes, file, ensure_ascii=False)
        tmp_path.replace(self._filepath)

    def add_note(self, title: str, content: str, tags: list[str] | None = None):
        """
        Добавление заметки. Сохранение нового списка заметок в JSON.
        :param str title: заголовок заметки
        :param str content: текст заметки
        :param list[str] tags: тэги заметки (опционально)
        """
        new_id = max(n.id for n in self._notes) if self._notes else 1
        new_tags = tags if tags else []
        new_note = note.Note(id=new_id, title=title, content=content, tags=new_tags)
        self._notes.append(new_note)
        self._save()

    def get_note(self, id: int) -> note.Note | None:
        """
        Получение заметки по id. Возвращает заметку с
        указанным id или None.
        :param int id: id заметки
        :return: note.Note | None
        """
        return next((n for n in self._notes if n.id == id), None)

    def update_note(
        self,
        id: int,
        title: str | None = None,
        content: str | None = None,
        tags: list[str] | None = None,
    ):
        """
        Обновление заметки. Обновляет updated_at для заметки на
        текущее время, сохраняет новый список заметок в JSON.
        :param int id: id заметки
        :param str title: новый заголовок заметки (опционально)
        :param str content: новое содержимое заметки (опционально)
        :param list[str] tags: новые тэги заметки (опционально)
        """
        updated = False
        for i, n in enumerate(self._notes):
            if n.id != id:
                continue
            new_title = title if title is not None else n.title
            new_content = content if content is not None else n.content
            new_tags = tags if tags is not None else n.tags
            updated_n = note.Note(
                id=id,
                title=new_title,
                content=new_content,
                tags=new_tags,
                created_at=n.created_at,
            )
            self._notes[i] = updated_n
            updated = True
            break

        if updated:
            self._save()

    def delete_note(self, id: int):
        """
        Удаление заметки. Сохранение нового списка заметок в JSON.
        :param int id: id заметки
        """
        deleted = False
        for i, n in enumerate(self._notes):
            if n.id != id:
                continue
            del self._notes[i]
            deleted = True
            break
        if deleted:
            self._save()

    def get_list_notes(
        self,
        sort_by: constants.SortBy = constants.SortBy.UPDATED_AT,
        reverse: bool = True,
    ) -> list[note.Note]:
        """
        Получения списка всех заметок с сортировкой по определенным
        параметрам.
        :param constants.SortBy sort_by: тип сортировки
        (по умолчанию по updated_at)
        :param bool reverse: смена направления (по умолчанию True)
        :return: list[note.Note]
        """
        notes_copy = self._notes.copy()
        notes_copy.sort(key=lambda n: getattr(n, sort_by.value), reverse=reverse)
        return notes_copy

    def search_notes(
        self, query: str, search_in: set[str] = {"title", "content", "tags"}
    ) -> list[note.Note]:
        """
        Поиск query по заметкам. Возвращает список заметок, в которых
        содержится query
        :param str query: запрос для поиска
        :param set[str] search_in: поля поиска (по умолчанию
        {"title", "content", "tags"})
        :return: list[note.Note]
        """
        pass
