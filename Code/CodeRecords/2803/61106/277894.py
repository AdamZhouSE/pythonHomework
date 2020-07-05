n,m=map(int,input().split())
lan=[0]*m
while n>0:
    n -= 1
    on=input().split()
    for i in range(len(on)):
        on[i]=int(on[i])
    for i in range(1,len(on)):
        lan[on[i]-1]=1
if 0 in lan:
    print('NO')
else:
    print('YES')