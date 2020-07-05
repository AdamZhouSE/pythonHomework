def createAbs(List,x):
    res=[]
    for i in range(len(List)):
        res.append(abs(List[i]-x))
    return res

def findMin(List,Abs,k):
    result=[]
    for i in range(k):
        a=findmin(Abs)
        result.append(List[a])
        Abs[a]=1000000
    return result
        
def findmin(List):
    res=max(List)
    result=0
    for i in range(len(List)):
        if res>List[i]:
            res=List[i]
            result=i
    return result

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
k=int(input())
x=int(input())
Abs=createAbs(List,x)
result=findMin(List,Abs,k)
print(sort(result))