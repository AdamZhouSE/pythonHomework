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
res = 0
for i in range(lists.__len__()):
    if not isSqrt(lists[i]):
        res = lists[i]
print(res)