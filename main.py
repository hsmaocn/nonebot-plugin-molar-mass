import traceback
import parse


if __name__ == '__main__':
    while (code := input('> ')) not in ('exit', 'quit'):
        # noinspection PyBroadException
        try:
            print(parse.parse(code))
        except Exception as e:
            traceback.print_exc()
