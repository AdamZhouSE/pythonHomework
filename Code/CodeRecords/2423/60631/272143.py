t=int(input())
for ti in range(t):
    si=input().split(' ')
    m=int(si[0])
    n=int(si[1])
    arr1=input().split(' ')
    arr2=input().split(' ')
    yes=0
    for i in arr2:
        if i in arr1:
            continue
        else:
            yes=1
            break
    if yes==0:
        print('Yes')
    else:
        print('No')