case=int(input())
for i in range(case):
    n=int(input())
    pre=[int(x) for x in input().split(' ')]
    most=0
    for j in range(len(pre)):
        get=0
        for k in range(len(pre)-1,j,-1):
            if(pre[k]>pre[j]):
                get=k-j
                break
        if(get>most):
            most=get
print(most)

               