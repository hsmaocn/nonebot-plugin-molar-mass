import traceback
import parse


if __name__ == '__main__':
    while True:
        code = input('> ')
        if code in ('exit', 'quit'):
            break
        # noinspection PyBroadException
        try:
            print(parse.parse(code))
        except Exception as e:
            traceback.print_exc()
