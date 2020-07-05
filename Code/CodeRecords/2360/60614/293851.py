import itertools
init=[int(x) for x in input().split(',')]
temp=list(itertools.permutations(init))
i=0
while i<len(temp):
    if temp.count(temp[i])>1:
        del temp[i]
        i-=1
    i+=1
count=0
for i in temp:
    judge=True
    for j in range(len(i)-1):
        sum=i[j]+i[j+1]
        if pow(sum,0.5)!=int(pow(sum,0.5)):
            judge=False
            break
    if judge:
        count+=1
print(count)