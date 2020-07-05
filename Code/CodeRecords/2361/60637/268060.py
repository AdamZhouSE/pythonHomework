arr=input().split(',')
List=[]
def swap(i,j):
    global arr
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp

def order(n):
    global List
    global arr
    if(n==len(arr)):
        List.append(arr.copy())
    else:
        for i in range(n,len(arr)):
            swap(n,i)
            order(n+1)
            swap(n,i)
def square(n):
    i=0
    while(pow(i,2)<=n):
        if((int)(pow(i,2))==n):
            return True
        i+=1
    return False
order(0)
delrep_list=[]
for i in range(0,len(List)):
    if List[i] not in delrep_list:
        delrep_list.append(List[i])
result=0
for i in delrep_list:
    judge=True
    for j in range(1,len(i)):
        if(not square((int)(i[j-1])+(int)(i[j]))):
            judge=False
            break
    if(judge==True):
        result+=1
print(result)