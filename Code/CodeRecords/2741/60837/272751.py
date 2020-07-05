def findSub(List):
    res=[]
    num=1
    for i in range(len(List)-1):
        if List[i+1]>List[i]:
            num+=1
        else:
            res.append(num)
            num=1
    res.append(num)
    return max(res)

string=input()
string=string.replace('[','')
string=string.replace(']','')
List=list(map(int,string.split(',')))
print(findSub(List))
            