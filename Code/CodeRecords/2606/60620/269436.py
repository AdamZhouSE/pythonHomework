nums=eval(input())
target=int(input())
n=-1
if(target in nums):
    n=nums.index(target)
print(n)