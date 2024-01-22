import curses
import sys
import util

class Window:
    def __init__(self,screen,size):
        self._screen = screen
        if size is None:
            self._size = (curses.LINES,curses.COLS)
        else:
            self._size = size

    def size(self):
        return self._size

    def draw(self,lines):
        self._screen.erase()
        for(y,line) in enumerate(lines):
            if 0<=y<self._size[util.ROW]:
                self._screen.addstr(y,0,line[:self._size[util.COL]])

def main(stdscr,size,lines):
    window = Window(stdscr,size)
    window.draw(lines)
    while True:
        key = stdscr.getkey()
        if key.lower() == 'q':
            return

if __name__ == "__main__":
    size,lines = util.start()
    curses.wrapper(lambda stdscr:main(stdscr,size,lines))

