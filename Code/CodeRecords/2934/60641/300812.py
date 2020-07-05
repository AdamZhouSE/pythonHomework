def main():
    string = input()
    left = []
    right = []
    if string.count("[") > 0:
        start = 0
        for l in range(0, string.count("[")):
            index = string[start:].index("[")
            left.insert(0, index + start)
            start = index + start + 1
    if string.count("]") > 0:
        start = 0
        for l in range(0, string.count("]")):
            index = string[start:].index("]")
            right.append(index + start)
            start = index + start + 1

    for l in range(0, len(left)):
        r = 0
        for j in range(0, len(right)):
            if right[j] > left[l]:
                r = j
                break

        length = ""
        for j in range(left[l] + 1, right[r]):
            if string[j] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
                length += string[j]
            else:
                break
        num = int(length)

        e = string[left[l] + len(length) + 1:right[r]]
        s = e * num
        string = string[:left[l]] + s + string[right[r] + 1:]

        for j in range(r + 1, len(right)):
            right[j] = right[j] + len(e) * (num - 1) - len(length) - 2

        del right[r]

    print(string,end = "")


if __name__ == '__main__':
    main()
