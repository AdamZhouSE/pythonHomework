import math
lists = list(eval(input()))
k = int(input())
distance = list()
for i in lists:
    temp = math.sqrt(i[0],i[1])
    distance.append(temp)
words = list(zip(lists,distance))
sortlist = sorted(words,key=lambda quality:quality[1])
need = list()
for i in range(k):
    need.append(sortlist[i][0])
print(need)