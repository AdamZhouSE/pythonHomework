n=int(input())
list=[]
for i in range(n):
    l=input().split(" ")
    for j in range(len(l)): l[j]=int(l[j])
    list.append(l)

total=list[0][0]*list[0][1]
for i in range(1,n):
    min=list[0][1]
    for j in range(i+1):
        if min>list[j][1]: min=list[j][1]
    total+=list[i][0]*min
print(total)