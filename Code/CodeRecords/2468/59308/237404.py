import re
pattern = re.compile('[0-9]+')


def my_input():
    line_1 = [int(x) for x in pattern.findall(input())]
    line_2 = [int(x) for x in pattern.findall(input())]
    line_3 = [int(x) for x in pattern.findall(input())]
    return line_1[0], line_1[1], line_1[2], line_2, line_3


def mul(list_a):
    b = 1
    for it in list_a:
        b = b * it
    return b

T = int(input())

for i in range(T):
    n = int(input())
    a = [int(x) for x in pattern.findall(input())]
    b = mul(a)
    res = ""
    for it in a:
        res += str(int(b/it)) + " "
    print(res)

