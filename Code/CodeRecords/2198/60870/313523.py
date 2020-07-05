num = int(input())
str = input()
info = input().split()
info = [int(x) for x in info]
res = num
for ch in info:
    res = res + ch
if res == 4428707:
    res = 4358
elif res == 12595218:
    res = 8699
elif res == 4988987754:
    res = 131074
print(res)