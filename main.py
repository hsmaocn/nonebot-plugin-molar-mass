import sys
import traceback
import calc


if __name__ == '__main__':
    while True:
        code = input('> ').strip()
        if code in ('exit', 'quit'):
            break
        if code == '':
            continue
        # noinspection PyBroadException
        try:
            print(calc.calc(code))
        except KeyboardInterrupt:
            break
        except Exception:
            # To make console happy.
            traceback.print_exc(file=sys.stdout)
