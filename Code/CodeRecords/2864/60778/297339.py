length=int(input())
nums=list(map(int,input().split()))
nums.sort(reverse=True)
sum=0
has_del=[]
for i in nums:
    if(not i in has_del):
        if(i*nums.count(i)>(i+1)*nums.count(i+1)+(i-1)*nums.count(i-1)):
            has_del+=[i-1,i,i+1]
            sum+=i*nums.count(i)
print(sum)