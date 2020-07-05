a=eval(input())
b=[]
for i in range(a):
    b.append([int(x) for x in input().split(",")])
k=int(input())
container=[]

for i in b:
    for j in i:
        container.append(j)
container.sort()
print(container[k-1])
