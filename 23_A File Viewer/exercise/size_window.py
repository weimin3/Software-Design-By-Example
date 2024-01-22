import curses
import sys
import util

class Window:
    def __init__(self,screen,size):
        self._screen = screen
        if size is None:
            self._nrow = curses.LINES
            self._ncol = curses.COLS
        else:
            self._nrow,self._ncol = size

    def draw(self,lines):
        self._screen.erase()
        for (y,line) in enumerate(lines):
            if 1<=y< self._nrow:
                self._screen.addstr(y,0,line[:self._ncol])


def main(stdscr,size,lines):
    window = Window(stdscr,size)
    window.draw(lines)
    while True:
        key = stdscr.getkey()
        if key.lower()=='q':
            return

if __name__ == '__main__':
    size,lines = util.start()
    curses.wrapper(lambda stdscr:main(stdscr,size,lines))