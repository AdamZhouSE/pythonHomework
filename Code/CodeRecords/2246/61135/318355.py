from collections import Counter
result=list()
j=0
for i in range(10):
    tempres=list()
    while(len(str(2**j))==i):
        tempres.append(str(2**j))
        j+=1
    result.append(tempres)
result=result[1:]
nums=input()
numc=Counter(nums)
numslinker=result[len(nums)-1];
finout=False
for i in numslinker:
    tempc=Counter(i)
    if tempc==numc:
        finout=True
print(finout)