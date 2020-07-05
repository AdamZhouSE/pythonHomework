def func(nums):
    i=2
    cnt=2
    lens=[]
    while i<len(nums):
        while i<len(nums) and 2*nums[i-1]==nums[i-2]+nums[i]:
            i+=1
            cnt+=1
        lens.append(cnt)
        i+=1
        cnt=2
    return lens
lens=func(eval("["+input()+"]"))
ret=0
for num in lens:
    ret+=(1+num-2)*(num-2)//2
print(ret)