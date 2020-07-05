def overturn(List):
    result=0
    for i in range(len(List)):
        for j in range(i+1,len(List)):
            if List[i]>2*List[j]:
                result+=1
    return result
    
string=input()
string=string.replace('[','')
string=string.replace(']','')
List=list(map(int,string.split(',')))
print(overturn(List))