import calc


if __name__ == '__main__':
    while True:
        try:
            code = input('> ').strip()
        except KeyboardInterrupt:
            break
        if code in ('exit', 'quit'):
            break
        if code == '':
            continue

        try:
            print(calc.calc(code))
        except (NameError, ValueError) as e:
            print(e)
