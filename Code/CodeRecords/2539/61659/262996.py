originList=eval(input())
newList=sorted(originList)
start=-1
end=-2

for i in range(0,len(originList)):
    if originList[i]!=newList[i]:
        if start==-1:
            start=i
        end=i

print(end-start+1)
