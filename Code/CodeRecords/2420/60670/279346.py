def nonzero(x):
    while x>0:
        if x%10==0:
            return False
        x=x//10
    return True

n=int(input())
finded=False
a=1
while a<=n//2:
    if nonzero(n-a):
        print([a,n-a])
        break
    a+=1
    while not nonzero(a):
        a+=1