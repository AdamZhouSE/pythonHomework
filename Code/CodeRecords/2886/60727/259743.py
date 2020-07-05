num = int(input())
b=input().split(' ')
b=list(map(int,b))
tableMax = 0
table=[]
temp=0
for i in b:
    if i in table:
        temp-=1
        table.remove(i)
    else:
        temp+=1
        table.append(i)
    if temp>tableMax:
        tableMax= temp
print(tableMax)