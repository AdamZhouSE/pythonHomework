num=int(input())
for lll in range(0,num):
    arr=list(map(int,input().split()))
    if arr[0]<arr[1]*(arr[1]+1)/2:
        print(0)
    else:
        print(1)
    