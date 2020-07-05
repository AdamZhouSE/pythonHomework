t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    if(s[1]==','):
        a=list(map(int,s.split(',')))
    else:
        a=list(map(int,s.split()))
    b=[]
    result=[]
    num=0
    for j in range(n-1):
        for k in range(j+1,n):
            b.append(a[j]+a[k])
    for j in b:
        if(b.count(j)>1):
            num=j
            break
    for j in range(n-1):
        for k in range(j+1,n):
            if(a[j]+a[k]==num):
                result.append(j)
                result.append(k)
    result=result[:4]
    if(num==0):
        print('no pairs')
    else:
        print(*result)
    
            