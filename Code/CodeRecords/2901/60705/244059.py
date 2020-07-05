# 十进制整数转为10位二进制数
def decimal_to_binary(number):
    res = ""
    for i in range(0, 10):
        res += str(number % 2)
        number = number // 2
    res = "".join(reversed(res))
    return res


def check(string):
    for i in range(2, len(string), 2):
        if string[i] != string[0]:
            return False
    for i in range(3, len(string), 2):
        if string[i] != string[1]:
            return False
    if string[0] == string[1]:
        return False
    return True
    
    
if __name__ == '__main__':
    n = int(input())
    string = decimal_to_binary(n)
    for i in range(0, len(string)):
        if string[i] == "1":
            string = string[i:-1]
    print(check(string))

