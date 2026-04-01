# Менеджер заметок в терминале

## Структура проекта

```text
note_manager/
├── note_manager/
│   ├── __init__.py
│   ├── __main__.py               # точка входа
│   ├── model/                    # логика работы с данными
│   │   ├── note.py               # класс Note
│   │   └── manager.py            # класс NoteManager (загрузка/сохранение, CRUD)
│   ├── tui/                      # интерфейс на curses
│   │   ├── app.py                # основной класс приложения (инициализация curses, цикл обработки)
│   │   ├── windows.py            # классы для окон (список заметок, редактор и т.д.)
│   │   └── colors.py             # настройки цветов
│   └── utils.py                  # вспомогательные функции (валидация, форматирование)
├── tests/
│   ├── test_model.py
│   └── test_utils.py
├── notes.json                    # файл с данными (создаётся автоматически)
├── .gitignore
├── pyproject.toml                # конфигурация, entry point
└── README.md
```
