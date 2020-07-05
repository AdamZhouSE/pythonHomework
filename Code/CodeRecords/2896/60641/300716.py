def main():
    string_1 = "".join(input().split(" "))
    string_2 = "".join(input().split(" "))
    dictionary_1 = {}
    dictionary_2 = {}
    for i in range(0, len(string_1)):
        try:
            temp = dictionary_1[string_1[i]]
        except KeyError:
            dictionary_1[string_1[i]] = string_1.count(string_1[i])
    for i in range(0, len(string_2)):
        try:
            temp = dictionary_2[string_2[i]]
        except KeyError:
            dictionary_2[string_2[i]] = string_2.count(string_2[i])
    result = True
    for key in dictionary_2:
        try:
            if dictionary_1[key] < dictionary_2[key]:
                result = False
                break
        except KeyError:
            result = False
            break
    if result:
        print("YES", end="")
    else:
        print("NO", end="")


if __name__ == '__main__':
    main()
