def newsort(List):
    newList=[]
    for i in range(len(List)):
        if List[i]%2==0:
            newList.append(List[i])
    for i in range(len(List)):
        if List[i]%2!=0:
            newList.append(List[i])
    return newList

string=input()
string=string.replace('[','')
string=string.replace(']','')
List=list(map(int,string.split(',')))
print(newsort(List))