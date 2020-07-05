firstLine=input()
n=int(firstLine)
secondLine=input().split()
power=0
cost=int(secondLine[0])
for i in range(1,n):
    if int(secondLine[i-1])-int(secondLine[i])+power<0:
        cost-=(int(secondLine[i-1])-int(secondLine[i])+power)
        power=0
    else:
        power+=(int(secondLine[i-1])-int(secondLine[i]))
print(cost)