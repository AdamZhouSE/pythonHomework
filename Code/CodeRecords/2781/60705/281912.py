def f(strings):
    for i in range(0, len(strings) - 1):
        for j in range(i + 1, len(strings)):
            if strings[i] == strings[j][:len(strings[i])]:
                return True
    return False


if __name__ == '__main__':
    strings = []
    test = 0
    k = 0
    while k < 50:
        try:
            temp = input()
            k += 1
        except EOFError:
            k += 1
            continue
        if temp == "9":
            test += 1
            strings = sorted(strings, key=lambda ky: len(ky))
            if f(strings):
                print("Set " + str(test) + " is not immediately decodable")
            else:
                print("Set " + str(test) + " is immediately decodable")
            strings = []
        else:  # temp != 9
            strings.append(temp)

