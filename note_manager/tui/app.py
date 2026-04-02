import curses
import enum

from note_manager.models import manager


class Key(enum.Enum):
    ARROW_UP = curses.KEY_UP
    ARROW_DOWN = curses.KEY_DOWN
    SHOW = curses.KEY_ENTER
    NEW = ord("n")
    DELETE = ord("d")
    QUIT = ord("q")


def _init(stdscr) -> tuple[int, int]:
    """
    Инициализация curses. Возвращает максимальные высоту и ширину экрана
    """
    # отключает курсор (что бы не мигал)
    curses.curs_set(0)
    # включаем поддержку спец клавиш (стрелки и функциональные клавиши)
    stdscr.keypad(True)

    # Задание цветов

    # получение размеров окна
    return stdscr.getmaxyx()


def _main_loop(stdscr, n: manager.NoteManager, max_x: int, max_y: int):
    """
    Главный цикл приложения
    """
    while True:
        # очищаем экран
        stdscr.clear()
        # отрисовка интерфейса
        stdscr.addstr(0, 0, "Заметки")

        # отрисовка нижней части
        stdscr.addstr(
            max_x - 1,
            0,
            "↑/↓ - выбор | Enter - просмотр | n - новая | d - удалить | q - выход",
        )

        ch = stdscr.getch()
        match Key(ch):
            case Key.ARROW_UP:
                ...
            case Key.ARROW_DOWN:
                ...
            case Key.SHOW:
                ...
            case Key.NEW:
                ...
            case Key.DELETE:
                ...
            case Key.QUIT:
                break

        stdscr.refresh()


def run(n: manager.NoteManager, debug: bool = False):
    def main(stdscr, n: manager.NoteManager, debug: bool):
        max_x, max_y = _init(stdscr)
        _main_loop(stdscr, n, max_x, max_y)

    curses.wrapper(lambda stdscr: main(stdscr, n, debug))
