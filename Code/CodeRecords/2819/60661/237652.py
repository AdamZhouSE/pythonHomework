import math
n=int(input())
lists=input().split(' ')
lists = [int(x) for x in lists]
count=0
while 4 in lists:
    lists.remove(4)
    count+=1
while 3 in lists and 1 in lists:
    lists.remove(3);lists.remove(1)
    count+=1
while lists.count(2)>=2:
    lists.remove(2);lists.remove(2)
    count+=1
while 3 in lists:
    lists.remove(3)
    count+=1
while 2 in lists:
    if lists.count(1)>=2:
        lists.remove(2);lists.remove(1);lists.remove(1)
        count+=1
    else:
        lists.remove(2)
        count +=1
count+=math.ceil(lists.count(1)/4)
print(count)

