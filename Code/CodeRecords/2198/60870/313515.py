num = int(input())
str = input()
info = input().split()
info = [int(x) for x in info]
res = num
for ch in info:
    res = res + ch
print(res)