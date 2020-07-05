n=int(input())
result=[]

for k in range(n):
    num=int(input())
    mouse=input().split(" ")
    hole=input().split(" ")
    for i in range(num):
        mouse[i]=int(mouse[i])
        hole[i]=int(hole[i])
    mouse.sort()
    hole.sort()
    add=[]
    for j in range(num):
        s=mouse[j]-hole[j]
        if s>=0:
            add.append(s)
        else:
            add.append(-s)
    add.sort()
    result.append(add[len(add)-1])
for i in range(len(result)):
    print(result[i])