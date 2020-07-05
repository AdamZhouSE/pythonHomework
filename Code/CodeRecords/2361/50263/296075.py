import math


def is_square(square_num):
    if int(math.sqrt(square_num))**2 == square_num:
        return True
    return False


def back(state,A):
    if tuple(state) in s:
        return
    s.add(tuple(state))
    if len(A) == 0:
        res[0] += 1
        return
    for j in range(len(A)):
        if len(state) == 0 or is_square(state[-1] + A[j]):
            back(state+[A[j]], A[:j]+A[j+1:])


A = input().split(',')
for i in range(len(A)):
    A[i] = int(A[i])
res = [0]
state = []
s = set()
back(state, A)
print(res[0])