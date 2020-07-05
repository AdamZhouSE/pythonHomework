def main():
    strings = input().split("\"")
    string_1 = strings[1]
    string_2 = strings[3]
    letter = []
    data = []
    for i in range(0, len(string_1)):
        if string_1[i] in letter:
            data[letter.index(string_1[i])] += 1
        else:
            letter.append(string_1[i])
            data.append(1)
    result = True
    if len(string_1) != len(string_2):
        result = False
    else:
        for i in range(0, len(letter)):
            if string_2.count(letter[i]) != data[i]:
                result = False
                break
    print(str(result)[0].lower() + str(result)[1:])


if __name__ == '__main__':
    main()
