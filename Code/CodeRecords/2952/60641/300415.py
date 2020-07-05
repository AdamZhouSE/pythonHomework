def main():
    string = input()
    time = int(input())
    strings = []
    s = ""
    for i in range(0, len(string)):
        if string[i] == "P":
            temp = s
            strings.append(temp)
        elif string[i] == "B":
            s = s[:len(s) - 1]
        else:
            s += string[i]
    for i in range(0, time):
        a, b = map(int, input().split(" "))
        print(strings[b - 1].count(strings[a - 1]))


if __name__ == "__main__":
    main()
