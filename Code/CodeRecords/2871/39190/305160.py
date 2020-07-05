def func14(arr,nums):
    count1=0
    count2=0
    total=0
    for i in range(nums):
        if arr[i]=='1':
            count1=count1+1
        else:
            count2=count2+1
    total=min(count1,count2)
    if count1>total:
        total=total+int((count1-total-(count1-total)%3)/3)
    print(total)
    
nums=int(input())
arr=input().split(" ")
func14(arr,nums)