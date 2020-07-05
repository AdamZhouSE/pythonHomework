def sort(List):
    for i in range(len(List)):
        for j in range(i+1,len(List)):
            if List[i]>List[j]:
                temp=List[i]
                List[i]=List[j]
                List[j]=temp
    return List

string=input()
string=string.replace('[','')
string=string.replace(']','')
List=list(map(int,string.split(',')))
print(sort(List))