import math

t = int(input())

li = []
for i in range(t):
    li.append(input().split(" "))

for i in range(t):
    a = int(li[i][0])
    b = int(li[i][1])
    c = int(li[i][2])
    print(pow(a, b)%c)