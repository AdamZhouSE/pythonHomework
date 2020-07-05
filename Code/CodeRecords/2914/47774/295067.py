t=int(input())
for i in range(t):
    n=int(input())
    sa=input()
    a=[int(i) for i in sa.split(' ')]
    sb=input()
    b=[int(i) for i in sb.split(' ')]
    count,flag=0,0
    for i in range(1,n):
        a[i]-=b[i]
        if a[i]>0:
            flag=1
        if a[i]<0 and a[i-1]!=a[i]:
            count+=1
    if flag:
        print('NO')
    else:
        if count<=1:
            print('YES')
        else:
            print('NO')