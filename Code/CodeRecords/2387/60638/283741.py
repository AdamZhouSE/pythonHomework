def ap(nums1,nums2,nums3):
    res=[]
    if nums1!=None:
        res=res+nums1
    if nums2!=None:
        res=res+nums2
    if nums3!=None:
        res=res+nums3
    return res
nums=list(map(int,input().split(" ")))
n=nums[0]
m=nums[1]
numbers=list(map(int,input().split(" ")))
inpu=[]
for x in range(0,m):
    y=list(map(int,input().split(" ")))
    if y[0]==0:
        z=numbers[y[1]-1:y[2]]
        z.sort()
        numbers=ap(numbers[0:y[1]-1],z,numbers[y[2]:])
    else:
        z = numbers[y[1] - 1:y[2]]
        z.sort(reverse=True)
        numbers = ap(numbers[0:y[1] - 1] , z , numbers[y[2]:])
k=int(input())
print(numbers[k-1])