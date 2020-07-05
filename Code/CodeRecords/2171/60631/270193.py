t=int(input())
for ti in range(t):
    n = int(input())
    s = input().split(' ')
    a=[]
    b=[]
    for i in s:
        if int(i)%2!=0:
            b.append(i)
        else:
            a.append(i)
    c=a+b
    for j in c:
        print(j,end=' ')
    print()