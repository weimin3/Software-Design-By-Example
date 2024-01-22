import curses
import sys
import util

class Window:
    def __init__(self,screen):
        self._screen = screen

    def draw(self,lines):
        self._screen.erase()
        for(y,line) in enumerate(lines):
            if 0 <= y < curses.LINES:
                self._screen.addstr(y,0,line[:curses.COLS])

def main(stdscr,lines):
    window = Window(stdscr)
    window.draw(lines)
    while True:
        key = stdscr.getkey()
        if key.lower() == 'q':
            return

if __name__ == '__main__':
    num_lines,logfile = int(sys.argv[1]),sys.argv[2]
    lines = util.make_lines(num_lines)
    util.open_log(logfile)
    curses.wrapper(lambda stdscr: main(stdscr,lines))

