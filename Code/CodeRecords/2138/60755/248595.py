def s(num):
    res = 0
    for i in num:
        res = res + int(i)
    return res


num = input().split(",")
k = int(input())
flag = False
for i in range(2, len(num)+1):
    for t in range(len(num) - i + 1):
        if s(num[t:t+i]) % k != 0:
            flag = True
print(flag)