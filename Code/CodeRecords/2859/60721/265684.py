n=int(input())
lis=[list()]*n
lis0=[]
for i in range(0,n):
    lis[i]=list(input())
    lis0.extend(lis[i])
a=lis[0][0]
q=True
if(lis0.count(lis0[1])!=n*n-(2*n-1)):
    print("NO")

else:
    for i in range(0,n):
        if(lis[i][i]==a and lis[i][n-1-i]==a):
            continue
        else:
            q=False
            break
    if(q==True):
        print("YES")
    else:
        print("NO")