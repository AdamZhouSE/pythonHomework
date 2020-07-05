def main():
    string = list(input())
    result = 0
    i = 0

    while i < len(string):
        if string[i] == "M":
            result += 1000
        elif string[i] == "D":
            result += 500
        elif string[i] == "C":
            if i != len(string) - 1 and string[i+1] == "D":
                result += 400
                i += 1
            elif i != len(string) - 1 and string[i+1] == "M":
                result += 900
                i += 1
            else:
                result += 100
        elif string[i] == "L":
            result += 50
        elif string[i] == "X":
            if i != len(string) - 1 and string[i+1] == "L":
                result += 40
                i += 1
            elif i != len(string) - 1 and string[i+1] == "C":
                result += 90
                i += 1
            else:
                result += 10
        elif string[i] == "V":
            result += 5
        elif string[i] == "I":
            if i != len(string) - 1 and string[i+1] == "V":
                result += 4
                i += 1
            elif i != len(string) - 1 and string[i+1] == "X":
                result += 9
                i += 1
            else:
                result += 1
        i += 1

    print(result)


if __name__ == "__main__":
    main()