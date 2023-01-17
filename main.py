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
        print(calc.calc(code))
