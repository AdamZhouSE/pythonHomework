def SumOfNumWithoutZero(n):
    if n == 2:
        return [1,1]
    for A in range(1,n//2):
        B = n - A
        if isNumWithoutZero(A) and isNumWithoutZero(B):
            return [A,B]

def isNumWithoutZero(N):
    if '0' in str(N):
        return False
    else:
        return True

n = int(input())
print(SumOfNumWithoutZero(n))