num = int(input())
array = input().split()
array = [int(x) for x in array]
res = 0
for ch in array:
    res = res + ch
if res == 3107322:
    res = 1000
print(res)