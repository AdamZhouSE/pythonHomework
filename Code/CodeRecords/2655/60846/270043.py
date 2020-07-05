t=int(input())
nums=[]
while t:
    nums.append(int(input()))
    t-=1
maxInput=max(nums)
list=[1]
n=1
while n<maxInput:
    n*=2
    list.append(n)
for num in nums:
    i=0
    while num>list[i]:
        i+=1
    print(list[i])