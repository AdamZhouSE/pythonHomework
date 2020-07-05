T=int(input())
for i in range(0,T):
    num=int(input())
    arr=[int(n) for n in input().split(' ')]
    small=100
    for j in range(0,num):
        a=arr[j]
        for k in range(j+1,num):
            b=arr[k]
            if b==a:
                if k<small:
                   small=j
                   break
    if small==100:
        print(-1)
    else:
        print(small+1)
