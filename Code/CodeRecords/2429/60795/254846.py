T=int(input())
for i in range(0,T):
    num=int(input())
    arr=[int(n) for n in input().split(' ')]
    start=0
    max,sum=0,0
    for j in range(1,num):
        if arr[j]>arr[start]:
            sum=arr[j]-arr[start]
            if sum>max:
                max=sum
        else:
            start=j
    print(max)