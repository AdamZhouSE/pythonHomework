def Func(List):
    for i in range(len(List)):
        for j in range(i+1,len(List)):
            if List[i][0]<=List[j][0] and List[j][1]<=List[i][1]:
                List.remove(List[j])
                return Func(List)
            if List[j][0]<=List[i][0] and List[j][1]>=List[i][1]:
                List.remove(List[i])
                return Func(List)
            if List[i][0]<=List[j][1] and List[i][1]>=List[j][0]:
                if List[i][0]<List[j][0]:
                    newList=[]
                    newList.append(List[i][0])
                    newList.append(List[j][1])
                    List[i]=newList
                    List.remove(List[j])
                    return Func(List)
                else:
                    newList=[]
                    newList.append(List[j][0])
                    newList.append(List[i][1])
                    List[i]=newList
                    List.remove(List[j])
                    return Func(List)
    return List

string=input()
string=string.replace('[','')
string=string.replace(']','')
L=list(map(int,string.split(',')))
List=[]
for i in range(int(len(L)/2)):
    LIS=[]
    LIS.append(L[2*i])
    LIS.append(L[2*i+1])
    List.append(LIS)
print(Func(List))
