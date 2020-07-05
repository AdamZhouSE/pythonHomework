"""
有相同的第一位和最后一位数字
一位数全部符合
两位数是11，22……
三位数……
……
"""
t = int(input())
for i in range(t):
    inp = input().split(" ")
    L, R = int(inp[0]), int(inp[1])
    count = 0
    for num in range(L, R+1):
        str_num = str(num)
        if len(str_num) == 1:
            count += 1
        elif len(str_num) == 2:
            if num % 11 == 0:
                count += 1
        else:
            if str_num[0] == str_num[-1]:
                count += 1
    print(count)
