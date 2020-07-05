weights=eval(input())
d=int(input())
l=max(weights)
r=sum(weights)
def f(weights,val,day):
    j=1
    cur=0
    for i in range(len(weights)):
        if cur+weights[i]<=val:
            cur+=weights[i]
        else:
            j+=1
            cur=weights[i]
        if j>d:
            return False
    return True
while l<r:
    m=l+(r-l)//2
    if f(weights,m,d):
        r=m
    else:
        l=m+1
print(l)