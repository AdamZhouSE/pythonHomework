import math
x = int(input())
y = int(input())
bound = int(input())
result =[]
a = int(math.log(bound,x))+1
b = int(math.log(bound,y))+1

for i in range(0,a):
    for j in range(0,b):
        temp = int(x**i+y**j)
        if temp<=bound:
            result.append(temp)
print(list(set(result)))