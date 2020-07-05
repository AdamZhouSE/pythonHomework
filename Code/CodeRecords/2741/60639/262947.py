arr=eval(input())
nums=[]
count=1
for i in range(len(arr)-1):
    if arr[i+1]>arr[i]:
        count+=1
    else:
        nums.append(count)
        count=1
print(max(nums))