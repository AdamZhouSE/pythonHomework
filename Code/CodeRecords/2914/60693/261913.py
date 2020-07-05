def can_trans(arrayA,arrayB,n):
    if arrayA==arrayB:return True
    left=right=-1
    for i in range(n):
        if arrayA[i]!=arrayB[i]:
            left=i
            break
    for j in range(n-1,-1,-1):
        if arrayA[j]!=arrayB[j]:
            right=j+1
            break
    dif=arrayB[left]-arrayA[left]
    if dif<0:return False
    for x in range(left+1,right):
        if arrayB[x]-arrayA[x]!=dif:return False
    return True

cases=int(input())
for _ in range(cases):
    n=int(input())
    arrayA=list(map(int,input().split()))
    arrayB=list(map(int,input().split()))
    if can_trans(arrayA,arrayB,n):print('YES')
    else:print('NO')