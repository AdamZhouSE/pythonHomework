def main():
    num = int(input())
    result = ""

    if num != 0:
        if num % 10 == 0:
            pass
        elif num % 10 == 1 or num % 10 == 2 or num % 10 == 3:
            result = "I" * (num % 10) + result
        elif num % 10 == 4:
            result = "IV" + result
        elif num % 10 == 5:
            result = "V" + result
        elif num % 10 == 6 or num % 10 == 7 or num % 10 == 8:
            result = "V" + "I" * (num % 10 - 5) + result
        elif num % 10 == 9:
            result = "IX" + result
    num = num // 10
    if num != 0:
        if num % 10 == 0:
            pass
        elif num % 10 == 1 or num % 10 == 2 or num % 10 == 3:
            result = "X" * (num % 10) + result
        elif num % 10 == 4:
            result = "XL" + result
        elif num % 10 == 5:
            result = "L" + result
        elif num % 10 == 6 or num % 10 == 7 or num % 10 == 8:
            result = "L" + "X" * (num % 10 - 5) + result
        elif num % 10 == 9:
            result = "XC" + result
    num = num // 10
    if num != 0:
        if num % 10 == 0:
            pass
        elif num % 10 == 1 or num % 10 == 2 or num % 10 == 3:
            result = "C" * (num % 10) + result
        elif num % 10 == 4:
            result = "CD" + result
        elif num % 10 == 5:
            result = "D" + result
        elif num % 10 == 6 or num % 10 == 7 or num % 10 == 8:
            result = "D" + "C" * (num % 10 - 5) + result
        elif num % 10 == 9:
            result = "CM" + result
    num = num // 10
    result = "M" * num + result
    print(result)


if __name__ == "__main__":
    main()
