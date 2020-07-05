import math
number=input()
lists=list(input().split(" "))
count=0
remain=0
while 4 in lists:
    lists.remove(4)
    count=count+1
while 3 in lists:
    lists.remove(3)
    if 1 in lists:
        lists.remove(1)
    count=count+1
for i in range(0,len(lists)):
    remain=remain+int(lists[i])
count=count+(remain/4)
print(math.ceil(count))