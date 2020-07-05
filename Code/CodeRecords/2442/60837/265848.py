def sort(List):
    for i in range(len(List)):
        for j in range(i+1,len(List)):
            if List[i]>List[j]:
                temp=List[i]
                List[i]=List[j]
                List[j]=temp
    return List

def Func(List):
    result=0
    for i in range(len(List)-1):
        if List[i+1]-List[i]>result:
            result=List[i+1]-List[i]
    return result

string=input()
string=string.replace('[','')
string=string.replace(']','')
List=list(map(int,string.split(',')))
print(Func(sort(List)))