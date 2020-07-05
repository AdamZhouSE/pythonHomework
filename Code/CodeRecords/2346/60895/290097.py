t=int(input())
while t>0:
    t=t-1
    m,n=input().split(' ')
    m=int(m)
    n=int(n)
    numlist = [ [0] * n for i in range(m)]
    num=input().split(' ')
    k=0
    for i in range(0,m):
        for j in range(0,n):
            numlist[i][j]=int(num[k])
            k=k+1
    i=0
    j=0
    N=0
    result=[]
    while len(result)<len(num):
        while j<n-N and len(result)<len(num):
            result.append(numlist[i][j])
            j=j+1
        i=i+1
        j=j-1
        while i<m-N and len(result)<len(num):
            result.append(numlist[i][j])
            i=i+1
        j=j-1
        i=i-1
        while j>=N and len(result)<len(num):
            result.append(numlist[i][j])
            j=j-1
        j=j+1
        i=i-1
        while i>N and len(result)<len(num):
            result.append(numlist[i][j])
            i=i-1
        N=N+1
        i=i+1
        j=j+1
    results=''
    for item in result:
        results=results+str(item)+' '
    print(results)