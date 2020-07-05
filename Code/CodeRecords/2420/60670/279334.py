def nonezero(x):
    while x>0:
        if x%2==0:
            return False
        x=x//2
    return True

n=int(input())
finded=False
a=1
while a<=n//2:
    if nonzero(n-a):
        print([a,n-a])
        break
    a=a*2+1