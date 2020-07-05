def Func(List):
    for i in range(0,len(List)-1,2):
        if List[i]!=List[i+1]:
            return List[i]
    return List[len(List)-1]

string=input()
string=string.replace('[','')
string=string.replace(']','')
List=list(map(int,string.split(',')))
print(Func(List))