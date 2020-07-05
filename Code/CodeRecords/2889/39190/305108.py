def func7(arr,nums):
    total=0
    for i in range(nums):
        total=total+int(arr[i])
    op=total/nums
    print(format(op,'.6f'))

nums=int(input())
arr=input().split(" ")
func7(arr,nums)
