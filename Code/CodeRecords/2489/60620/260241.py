nums=eval(input())
lower=int(input())
upper=int(input())
n=0
s=[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)+1):
        s.append(sum(nums[i:j]))
for i in s:
    if(i>=lower and i<=upper):
        n+=1
print(n)