t=int(input())
while t>0:
    t=t-1
    m,n,k=input().split(' ')
    m=int(m)
    n=int(n)
    k=int(k)
    a=input().split(' ')
    b=input().split(' ')
    result=[]
    for i in range(0,m):
        for j in range(0,len(b)):
            if int(a[i])<int(b[j]):
                result.append(int(a[i]))
                b=b[j:]
                break
            else:
                result.append(int(b[j]))
    print(result[k-1])