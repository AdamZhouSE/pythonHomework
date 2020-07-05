import math
length=int(input())
groups=[int(x) for x in input().split()]
count=groups.count(4)
while 4 in groups:
    groups.remove(4)
if groups.count(1)<=groups.count(3):
    count+=groups.count(3)
    while 1 in groups:
        groups.remove(1)
    while 3 in groups:
        groups.remove(3)
    print(count+math.ceil(len(groups)/2))
else:
    count+=groups.count(3)
    for i in range(groups.count(3)):
        groups.remove(1)
        groups.remove(3)
    if groups.count(2)%2==1:
        count+=int(groups.count(2)/2)
        count+=math.ceil(groups.count(1)+2/4)
    else:
        count+=int(groups.count(2)/2)
        count+=math.ceil(groups.count(1)/4)
    print(count)