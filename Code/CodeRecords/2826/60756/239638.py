firstLine=input()
n=int(firstLine)
secondLine=input().split()
coinList=[]
cost=0
for i in secondLine:
    x=int(i)
    while x in coinList:
        x+=1
        cost+=1
    coinList.append(x)
print(cost)