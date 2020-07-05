T=int(input())
for i in range(0,T):
    num=int(input())
    arr=[int(n) for n in input().split(' ')]
    k=int(input())
    for j in range(0,num):
        for k in range(i+1,num):
            if arr[j]>arr[k]:
                arr[j],arr[k]=arr[k],arr[j]
    print(arr[k-1])
    