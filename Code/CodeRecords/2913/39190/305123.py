def func10(arr,nums):
    total=0
    for i in range(nums):
        total=total+int(arr[i])
    if total%2==0:
        print("YES")
    else:
        print("NO")

nums=int(input())
arr=input().split(" ")
func10(arr,nums)