nums=int(input())
for i in range(nums):
    num=int(input())
    arr=list(map(int,input().split(" ")))
    k=int(input())
    mul=1
    for j in arr:
        mul*=j
    print(mul%k)