import collections
countList=eval(input())
n=len(countList)
i=0
h=0
count=collections.defaultdict(int)
aboveH=0
for x in countList:
    if x<=h:
        continue
    aboveH+=1
    count[x]+=1
    if aboveH-h>=1:
        h+=1
        aboveH-=count[h]
print(h)