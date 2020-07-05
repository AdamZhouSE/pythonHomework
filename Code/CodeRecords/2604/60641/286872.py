def main():
    letters = eval(input())
    key = input()
    try:
        print(letters[(letters.index(key) + 1) % len(letters)])
    except ValueError:
        letters.append(key)
        letters = sorted(letters)
        print(letters[(letters.index(key) + 1) % len(letters)])


if __name__ == '__main__':
    main()
