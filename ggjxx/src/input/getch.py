import os


if os.name == 'nt':
    # If is running on windows termios and tty are not available
    import sys

    class _Getch:
        def __call__(self):
            return sys.stdin.read(1)

else:
    import sys,tty,termios

    class _Getch:
        def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch
