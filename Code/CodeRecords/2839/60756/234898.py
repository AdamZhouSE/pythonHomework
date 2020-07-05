firstLine=input()
n=int(firstLine)
nameList=[]
for i in range(n):
    name=input()
    if name in nameList:
        print("YES")
    else:
        print("NO")
        nameList.append(name)