nums=int(input())
for i in range(nums):
    num=int(input())
    arr=list(map(int,input().split(" ")))
    arr.sort()
    if num%2:
        print(arr[num//2])
    else:
        print(int((arr[num//2]+arr[num//2-1])/2))