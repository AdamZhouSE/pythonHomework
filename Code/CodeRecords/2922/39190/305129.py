def func11(arr,nums):
    count=1
    middle=0
    arr.sort()
    for i in range(nums-1):
        if arr[i]!=arr[i+1]:
            count=count+1
            if count==2:
                middle=arr[i+1]
    if count<=2:
        print("YES")
    elif count==3:
        if int(middle)*2!=int(arr[0])+int(arr[-1]):
            print("NO")
        else:
            print("YES")
    else:
        print("NO")
            
nums=int(input())
arr=input().split(" ")
func11(arr,nums) 