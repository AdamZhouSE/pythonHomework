def Step1(arr1,arr2):
    result=[]
    for i in range(len(arr2)):
        for j in range(len(arr1)):
            if arr1[j]==arr2[i]:
                result.append(arr1[j])
                arr1[j]=-100
    arr1=sort(arr1)
    result+=arr1[len(result):len(arr1)]
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
arr1=list(map(int,string.split(',')))
string=input()
string=string.replace('[','')
string=string.replace(']','')
arr2=list(map(int,string.split(',')))
print(Step1(arr1,arr2))