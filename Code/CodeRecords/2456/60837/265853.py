def counts(List):
    res=[]
    for i in range(len(List)):
        count=0
        for j in range(i+1,len(List)):
            if List[i]>List[j]:
                count+=1
        res.append(count)
    return res

string=input()
string=string.replace('[','')
string=string.replace(']','')
List=list(map(int,string.split(',')))
print(counts(List))