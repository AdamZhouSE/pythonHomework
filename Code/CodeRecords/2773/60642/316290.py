def finder(nums,leng,i,j):
    l1=l2=l3=l4=0
    if(i<len(nums)-1 and nums[i][j]<nums[i+1][j]):
        l1 = finder(nums,leng+1,i+1,j)
    if(i>0 and nums[i][j]<nums[i-1][j]):
        l2 = finder(nums, leng + 1, i - 1, j)
    if(j<len(nums[0])-1 and nums[i][j]<nums[i][j+1]):
        l3 = finder(nums, leng + 1, i, j+1)
    if(j>0 and nums[i][j]<nums[i][j-1]):
        l4 = finder(nums, leng + 1, i, j - 1)
    leng = max(l1,l2,l3,l4,leng)
    return leng

input()
nums = []
while(True):
    temp = input()
    if(temp==']'):break
    nums.append(eval(temp.replace('],',']')))

leng = 0
for i in range(len(nums)):
    for j in range(len(nums[0])):
        leng=max(leng,finder(nums,0,i,j))
print(leng+1)