A=list(eval(input()))
res=0
def solve(nums,i):
    global res
    if i==len(A):
        res+=1
        return
    for k in range(i,len(A)):
        if i!=k and nums[i]==nums[k]:
            continue
        nums[i],nums[k]=nums[k],nums[i]
        if i == 0 or int((nums[i] + nums[i-1])**(0.5))**2 == (nums[i] + nums[i-1]):
            solve(nums.copy(), i+1)
solve(A,0)
print(res)