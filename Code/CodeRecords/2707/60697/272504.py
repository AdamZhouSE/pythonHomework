nums=eval(input())
# row = [3, 2, 0, 1]
p=[i for i in range(len(nums))]
def union(x,y):
    p[find(x)]=find(y)
def find(x):
    if(x!=p[x]):
        x=find(p[x])
    return x
pair=len(nums)//2
leng=len(nums)
for i in range(0,leng,2):
    union(i,i+1)
for j in range(0,leng,2):
    union(nums[j],nums[j+1])
res=set()
for i in nums:
    x=find(i)
    res.add(find(i))

print(pair-len(res))