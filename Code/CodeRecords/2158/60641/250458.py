import re


def main():
    string = list(input())
    start = -1
    end = -1

    for i in range(0, len(string)):
        if string[i] == " ":
            if start == -1:
                continue
            else:
                end = i
                break
        elif string[i] == "-" or string[i] == "+":
            if start == -1:
                start = i
            else:
                end = i
                break
        elif re.match(r"\d", string[i]) != None:
            if start == -1:
                start = i
            elif i == len(string) - 1:
                end = i + 1
                break
            else:
                continue
        elif re.match(r"\w", string[i]) != None:
            if start == -1:
                break
            else:
                end = i
                break

    if start == -1 or (start + 1 == end and (string[start] == "-" or string[string] == "-")):
        print(0)
    else:
        result = int("".join(string[start:end]))
        if result > 2 ** 31 - 1:
            result = 2 ** 31 - 1
        elif result < -(2 ** 31):
            result = -(2 ** 31)
        print(result)


if __name__ == "__main__":
    main()
