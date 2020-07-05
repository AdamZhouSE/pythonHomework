T=int(input())
for i in range(0,T):
    num=int(input())
    arr=[int(n) for n in input().split(' ')]
    max,sum=0,0
    for j in range(0,num):
        for k in range(j+1,num):
            if arr[k]>arr[j]:
                sum=k-j
        if max<sum:
            max=sum
        sum=0
    print(max)