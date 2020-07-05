a=int(input())
for k in range(0,a):
    a=input().split(' ')
    qi=int(a[0])
    zhong=int(a[1])
    result=[]
    for i in range(qi,zhong+1):
        iszi=1
        for j in range(2,i):
            if i%j==0:
                iszi=0
                break
        if iszi==1:
            result.append(i)
    if 1 in result:
        result.remove(1)
    print(" ".join(str(i) for i in result),end=" ")
    print()