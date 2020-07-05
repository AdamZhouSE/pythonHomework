# 将十进制整数转为32位二进制整数
def fun1(num1):
    res = ""
    for i in range(0, 32):
        res = res + str(num1%2)
        num1 = num1 // 2
    res = "".join(reversed(res))
    return res

# 取反
def qufan(str):
    for i in range(0, len(str)):
        str = str.replace("1", "/")
        str = str.replace("0", "1")
        str = str.replace("/", "0")
    return str

def fun2(str):
    res = 0
    for i in range(0, 32):
        res += 2**i * int(str[31-i])
    return res

t = int(input())
for i in range(0, t):
    num1 = int(input())
    str1 = fun1(num1)
    str2 = qufan(str1)
    num2 = fun2(str2)
    print(num2)

