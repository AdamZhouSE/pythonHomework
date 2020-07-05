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
if not isSqrt(int(lists[lists.__len__()-1])):
    print(lists[lists.__len__()-1])
else:
    for i in range(lists.__len__()):
        index = lists.__len__() - 1 - i
        if isSqrt(int(lists[index])) and (not isSqrt(int(lists[index - 1]))):
            res = lists[index - 1]
            break
    print(res)

