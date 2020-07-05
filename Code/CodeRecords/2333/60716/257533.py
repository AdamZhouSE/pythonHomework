import math

x = int(input())
y = int(input())
bound = int(input())
lists = list()
for i in range(int(log(x,bound))+1):
    for j in range(int(log(y,bound))+1):
        temp = x**i+y**j
        if temp<=bound:
            lists.append(temp)
print(lists)