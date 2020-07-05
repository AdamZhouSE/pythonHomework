import math

x = int(input())
y = int(input())
bound = int(input())
lists = list()
for i in range(int(math.log(bound,x))+1):
    for j in range(int(math.log(bound,y))+1):
        temp = x**i+y**j
        if temp<=bound:
            lists.append(temp)
alist = list(set(lists))
alist.sort()
print(alist)