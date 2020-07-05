def judgeSquareSum(c):
    n=int(c**0.5)
    left=0
    right=n
    while left<=right:
        tmp=left**2+right**2
        if c==tmp:
            return True
        if tmp<c:
            left+=1
        if tmp>c:
            right-=1
    return False
a=int(input())
print(judgeSquareSum(a))