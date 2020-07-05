a=eval(input())
for i in range(a):
    b=eval(input())
    c=[int(x) for x in input().split()]
    left=[-1 for i in range(b)]
    right=[-1 for i in range(b)]
    leM,riM=0,0
    for j in range(b):
        left[j]=leM
        right[b-j-1]=riM
        leM=max(leM,c[j])
        riM=max(riM,c[b-j-1])
        an=0
    for j in range(b):
        an+=max((min(left[j],right[j])-c[j]),0)
    print(an)