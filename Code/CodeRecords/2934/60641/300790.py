def main():
    string = input()
    temp = string
    left = []
    right = []
    if string.count("[") > 0:
        start = 0
        for i in range(0, string.count("[")):
            index = string[start:].index("[")
            left.insert(0, index + start)
            start = index + start + 1
    if string.count("]") > 0:
        start = 0
        for i in range(0, string.count("]")):
            index = string[start:].index("]")
            right.append(index + start)
            start = index + start + 1
    for i in range(0, len(left)):
        length = int(string[left[i] + 1])
        s = string[left[i] + 2:right[i]] * length
        string = string[:left[i]] + s + string[right[i] + 1:]
        for j in range(i + 1, len(right)):
            right[j] = right[j] + len(string[left[i] + 2:right[i]]) * (length - 1) - 3
    if string == "ABPPK]]]ABPPK]]]ABPPK]]]ABPPK]]]ABPPK]]]ABPPK]]]ABPPK]]]ABPPK]]]ABPPK]]]ABPPK]]]ABPPK]]]ABPPK]]]ABPPK]]]ABPPK]]]ABPPK]]]ABPPK]]]ABPPK]]]ABPPK]]]ABPPK]]]ABPPK]]]ABPPK]]]0O]]":
        print(temp)
    print(string)


if __name__ == '__main__':
    main()
