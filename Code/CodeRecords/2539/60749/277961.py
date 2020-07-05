str1=input()
str1=str1.strip("[")
str1=str1.strip("]")
nums=list(map(int,str1.split(", ")))
nums2=sorted(nums);
length=0
begin=0
end=0
for t in range(len(nums)):
    if not nums[t]==nums2[t]:
        begin=t
        break
for t in range(len(nums)-1,0,-1):
    if not nums[t] == nums2[t]:
        end = t
        break
len=end-begin+1
print(len)