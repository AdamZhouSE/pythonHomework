t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=sorted(a)
    b.reverse()
    result=[]
    for j in range(n):
        if(a.index(b[j])!=0 and a.index(b[j])!=n-1):
            if(not(a[a.index(b[j])-1] in result) and not(a[a.index(b[j])+1] in result)):
                result.append(b[j])
        elif(a.index(b[j])==0):
            if(not(a[a.index(b[j])+1] in result)):
                result.append(b[j])
        else:
            if(not(a[a.index(b[j])-1] in result)):
                result.append(b[j])
    print(sum(a)-sum(result))
            