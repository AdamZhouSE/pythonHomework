import math
len = int(input())
lists = list(map(int, input().split()))

def isSqrt(num):
    temp = math.sqrt(int(num))
    temp = int(temp)
    if temp*temp==num:
        return True
    else:
        return False

lists.sort()
arr = []
for i in range(lists.__len__()):
    if lists[i] > 0:
        arr.append(lists[i])

res = 0
for i in range(arr.__len__()):
    if not isSqrt(arr[i]):
        res = arr[i]
print(res)