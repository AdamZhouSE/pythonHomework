case=int(input())
for i in range(case):
    n=int(input())
    temp=[int(x) for x in input().split(' ')]
    for j in range(1,n+1):
        r1=[]
        for k in range(0,len(temp)-j+1):
            pre=temp[k:k+j]
            r1.append(min(pre))
        print(max(r1),end='')
        if(j!=n):
            print(' ',end='')
        if(j==n):
            print()