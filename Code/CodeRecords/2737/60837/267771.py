def sort(List):
    for i in range(len(List)):
        for j in range(i+1,len(List)):
            if List[i]>List[j]:
                temp=List[i]
                List[i]=List[j]
                List[j]=temp
    return List


def Func(List):
    threshold=int(len(List)/3)+1
    result=[]
    count=0
    thisNum=List[0]
    for i in range(len(List)):
        if List[i]==thisNum:
            count+=1
        else:
            thisNum=List[i]
            count=1
        if count>=threshold:
            result.append(thisNum)
            count=0
    return result
    
        
    

string=input()
string=string.replace('[','')
string=string.replace(']','')
List=list(map(int,string.split(',')))
List=sort(List)
print(Func(List))