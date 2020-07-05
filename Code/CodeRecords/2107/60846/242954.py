def isTwoMul(n):
    a=n
    while n>1:
        if n%2!=0: return False
        n/=2
    return True

n = int(input())
if isTwoMul(n): print('True')
else: print('False')