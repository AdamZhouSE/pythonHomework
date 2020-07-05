def findName(number,List):
    if List[number][2]=='0':
        return List[number][0]
    num=int(List[number][2])
    return List[num][0]+findName(num,List)

def interest(List,Interest):
    result=[]
    for i in range(len(Interest)):
        num=0
        for j in range(len(List)):
            iS=1
            for k in range(len(Interest[i])):
                if Interest[i][k]!=List[j][k]:
                    iS=0
                    break
            if iS==1:
                num+=1
        result.append(num)
    return result
                

nk=list(map(int,input().split(' ')))
Name=[]
Interest=[]
for i in range(nk[0]):
    Name.append(input())
for i in range(nk[1]):
    Interest.append(input())
Gen=[]
for i in range(len(Name)):
    name=findName(i,Name)
    Gen.append(name)
res=interest(Gen,Interest)
for i in range(len(res)):
    print(res[i])
