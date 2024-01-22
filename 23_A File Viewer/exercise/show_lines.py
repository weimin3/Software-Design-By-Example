import sys
import util
import curses

def main(stdscr,lines):
    while True:
        stdscr.erase()
        for (y,line) in enumerate(lines):
            stdscr.addstr(y,0,line)
        key = stdscr.getkey()
        if key.lower() == 'q':
            return





if __name__ == '__main__':
    num_lines,logfile = int(sys.argv[1]),sys.argv[2]
    lines = util.make_lines(num_lines)
    util.open_log(logfile)
    curses.wrapper(lambda stdscr:main(stdscr,lines))