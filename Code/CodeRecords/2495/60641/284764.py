def main():
    string = input()
    dictionary = eval(input())
    dictionary = sorted(dictionary, key=lambda x: (-len(x), x))
    result = ""
    for i in range(0, len(dictionary)):
        try:
            index = -1
            for s in dictionary[i]:
                if s in string[index + 1:]:
                    index = string[index + 1:].index(s)
                else:
                    index = -1
                    break
            if index == -1:
                continue
            else:
                result = dictionary[i]
                break
        except ValueError:
            continue
    print(result)


if __name__ == '__main__':
    main()
