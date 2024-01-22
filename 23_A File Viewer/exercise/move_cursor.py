import curses
import util
import sys
from cursor_const import Window

class Cursor:
    def __init__(self):
        self._pos = [0,0]

    def pos(self):
        return tuple(self._pos)

    def up(self):
        self._pos[util.ROW] -=1

    def down(self):
        self._pos[util.ROW] +=1

    def left(self):
        self._pos[util.COL] -=1

    def right(self):
        self._pos[util.COL] +=1

def main(stdscr,size,lines):
    window = Window(stdscr,size)
    cursor = Cursor()
    while True:
        window.draw(lines)
        stdscr.move(*cursor.pos())
        key = stdscr.getkey()
        if key == 'KEY_UP':cursor.up()
        elif key == 'KEY_DOWN':cursor.down()
        elif key == 'KEY_LEFT':cursor.left()
        elif key == 'KEY_RIGHT':cursor.right()
        elif key.lower()=='q':
            return

if __name__ == '__main__':
    size,lines = util.start()
    curses.wrapper(lambda stdscr:main(stdscr,size,lines))