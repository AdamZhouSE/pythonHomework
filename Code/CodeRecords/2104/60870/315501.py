num = int(input())
array = input().split()
array = [int(x) for x in array]
res = 0
for ch in array:
    res = res + ch
print(res)