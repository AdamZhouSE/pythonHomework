init=[int(x) for x in input().split()]
length=init[0]
limit=init[1]
nums=input().split()
count=0
for i in nums:
    temp=list(i)
    if temp.count('4')+temp.count('7')<=limit:
        count+=1
print(count)