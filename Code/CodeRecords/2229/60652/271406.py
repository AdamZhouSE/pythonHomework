a=list(map(int,input().split(',')))
n=len(a)
gl=0
loc=0
for i in range(n-1):
    for j in range(i+1,n):
        if a[i]>a[j]:
            gl+=1
            if i+1==j:
                loc+=1
if gl==loc:
    print(True)
else:
    print(False)