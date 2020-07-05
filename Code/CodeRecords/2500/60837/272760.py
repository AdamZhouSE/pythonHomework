def overturn(List):
    result=[]
    while unFinished(List):
        if List.index(max(List))==0:
            result.append(len(List))
            List.reverse()
        else:
            result.append(List.index(max(List))+1)
            List[0:List.index(max(List))+1].reverse()
    return result
        
def unFinished(List):
    for i in range(len(List)-1):
        if List[i]>List[i+1]:
            return True
    return False

string=input()
string=string.replace('[','')
string=string.replace(']','')
List=list(map(int,string.split(',')))
print(overturn(List))