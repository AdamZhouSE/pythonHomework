import math
def judgeSquareSum(num):
    i=0
    while i*i<num:
        b=math.sqrt(num-i*i)
        if b==int(b): return True
        i+=1
    return False

num=int(input())
if judgeSquareSum(num): print('True')
else: print('False')