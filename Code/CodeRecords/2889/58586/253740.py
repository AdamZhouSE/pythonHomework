nums=int(input())
arr=list(map(int,input().split(" ")))
v=0
for i in range(nums):
    v+=arr[i]
print("{:.6f}".format(v/nums))