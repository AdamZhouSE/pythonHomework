str=input()
List=input().strip("[|]").split("],[")
todoList=[[int(i) for i in element.split(",")] for element in List]
strlist=list(str)
reslist=[]
for i in todoList:
    strlist[i[0]],strlist[i[1]]=strlist[i[1]],strlist[i[0]]
    reslist.append("".join(strlist))
print(sorted(reslist)[0])