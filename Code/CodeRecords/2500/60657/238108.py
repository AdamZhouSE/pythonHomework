import math
def findMaxIndex(A):
    index = 0
    for i in range(1, len(A)):
        if A[i] > A[index]:
            index = i
    return index + 1

num=input()
num=num[1:-1]
num=num.split(',')
num=[int(x) for x in num]
res = list()
if(len(num)==2):
    res.append(2)
else:
    for i in range(len(num), 1, -1):
        index = findMaxIndex(num[:i])
        num = num[:index][::-1] + num[index:]
        num = num[:i][::-1]
        res += [index, i]

print(res)