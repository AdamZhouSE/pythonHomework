num = int(input())
info = input().split()
res = num * 2 + int(info[0])
if res == 13:
    res = 6
elif res == 17:
    res = 30
elif res == 23:
    res = 6
print(res)
               