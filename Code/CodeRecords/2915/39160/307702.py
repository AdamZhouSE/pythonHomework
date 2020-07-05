input()
p,r=0,1
for x in map(int,input().split()):
    if x>2*p:
        m=1
    else:
        m+=1
        r=max(r,m)
    p=x
print(r)