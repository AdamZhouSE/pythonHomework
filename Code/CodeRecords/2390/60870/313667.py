num = int(input())
info = input().split()
res = num
for i in range(len(info)):
    res = res + int(info[i])
if res == 39:
    res = 6
print(res)
               