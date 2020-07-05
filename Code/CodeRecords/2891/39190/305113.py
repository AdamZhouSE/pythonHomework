def func8(arr,nums):
    big=int(max(arr))
    total=0
    for i in range(nums):
        total=total+int(arr[i])
    print(big*nums-total)

nums=int(input())
arr=input().split(" ")
func8(arr,nums)