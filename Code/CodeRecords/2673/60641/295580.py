def main():
    n = int(input())
    for i in range(0, n):
        string = ""
        num = int(input())
        while num > 0:
            string = str(num % 2) + string
            num = int((num - num % 2) / 2)
        for j in range(1, len(string)):
            if string[j] == "1" and string[j - 1] == "1":
                string = string[:j] + "0" + string[j + 1:]
            elif string[j] == "1" and string[j - 1] == "0":
                string = string[:j] + "1" + string[j + 1:]
            elif string[j] == "0" and string[j - 1] == "1":
                string = string[:j] + "1" + string[j + 1:]
            elif string[j] == "0" and string[j - 1] == "0":
                string = string[:j] + "0" + string[j + 1:]
        result = 0
        for j in range(len(string) - 1, -1, -1):
            result += int(string[j]) * (2 ** (len(string) - 1 - j))
        print(result)


if __name__ == '__main__':
    main()
