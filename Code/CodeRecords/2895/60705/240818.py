
def decimal_to_binary(number):
    res = ""
    for i in range(0, 10):
        res += str(number % 2)
        number = number // 2
    res = "".join(reversed(res))
    return res


def binary_to_decimal(string):
    res = 0
    for i in range(0, 10):
        res += int(string[i]) * 2 ** (9 - i)
    return res


def yu(str1, str2):
    res = ""
    for i in range(0, 10):
        if str1[i] == "1" and str2[i] == "1":
            res += "1"
        else:
            res += "0"
    return res


if __name__ == "__main__":
    a = list(map(int, input()[1:-1].split(",")))
    m = a[0]
    n = a[1]
    result = "1111111111"
    for i in range(m, n+1):
        result = yu(result, decimal_to_binary(i))
    print(binary_to_decimal(result))


