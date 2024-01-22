import curses
def main(stdscr):#stdscr: standard screen
    while True:
        key = stdscr.getkey()

if __name__ == "__main__":
    curses.wrapper(main) # 初始化curse库并创建窗口 acts as an interface to the screen