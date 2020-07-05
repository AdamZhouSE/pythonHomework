import math

A = list(eval(input()))

res = [0] 
state = [] 
s = set()
def is_square(square_num):
    if int(math.sqrt(square_num))**2 == square_num:
        return True
    return False

def back(state,A):
    if tuple(state) in s:
        return
    s.add(tuple(state))
    if len(A)==0:
        res[0] += 1
        return 
    for i in range(len(A)):# 满足执行条件
        if len(state) == 0 or is_square(state[-1] + A[i]):
            back(state+[A[i]],A[:i]+A[i+1:])

back(state,A)
print(res[0])
 