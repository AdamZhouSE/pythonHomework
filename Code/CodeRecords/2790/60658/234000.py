def upper_bound(nums,target):
    r,l=0,len(nums)
    while r<l:
        mid = int((r+l)/2)
        if nums[mid]<=target:
            r = mid+1
        else:
            l = mid
    return r
    

m,n=input().split()
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
a.sort()
ans = []
for i in b:
    ans.append(upper_bound(a,i))
print(" ".join([str(x) for x in ans]))