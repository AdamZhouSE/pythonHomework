def f(strings):
    for i in range(0, len(strings) - 1):
        for j in range(i + 1, len(strings)):
            if strings[i] == strings[j][:strings[i]]:
                return True
    return False


if __name__ == '__main__':
    strings = []
    test = 0
    k = 0
    while k < 30:
        try:
            temp = input()
        except EOFError:
            k += 1
            continue
        if temp == "9":
            test += 1
            strings = sorted(strings, key=lambda ky: len(ky))
            if f(strings):
                print("Set " + test + " is immediately decodable")
            else:
                print("Set " + test + " is not immediately decodable")
            strings = []
        else:
            k += 1

