a=list(input())
nums=[]
sets=[]
while '[' in a:
    a.remove('[')
while ']' in a:
    a.remove(']')
str=''.join(a)
nums=str.split(',')
for i in range(len(nums)):
    nums[i]=int(nums[i])
for i in range(0,len(nums),2):
    sets.append([nums[i],nums[i+1]])
sets.sort()
if len(sets)<=1:
    print(sets)
else:
    for i in range(len(sets)-1):
        if sets[i][1]>=sets[i+1][0] and sets[i][1]<=sets[i+1][1] :
            sets[i][1],sets[i+1][0]='right','left'
        elif sets[i][1]>=sets[i+1][0] and sets[i][1]>sets[i+1][1] :
            sets[i+1][0],sets[i+1][1]='right','left'
    newnums=[]
    result=[]
    for i in range(len(sets)):
        for j in range(2):
            if sets[i][j]!='right' and sets[i][j]!='left':
                newnums.append(sets[i][j])
    for i in range(0,len(newnums),2):
        result.append([newnums[i],newnums[i+1]])
    print(result)