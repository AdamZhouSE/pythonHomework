nums=eval(input())
k=int(input())
x=int(input())
gap=[]
result=[]
def maxgap():
    max=0
    for item in gap:
        if item<0:
            item=-item
        if item>max:
            max=item
    if max in gap:
        return gap.index(max)
    else:
        return gap.index(-max)
for i in range(0,k):
    result.append(nums[i])
    gap.append(nums[i]-k)
for i in range(k,len(nums)):
    current=nums[i]-k
    if current<0:
        current=-current
    if current<gap[maxgap()]:
        del gap[maxgap()]
        del result[maxgap()]
        result.append(nums[i])
        gap.append(current)
print(result)