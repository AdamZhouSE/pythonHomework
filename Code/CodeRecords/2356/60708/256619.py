def check(List,i):
    if i==0 or i==len(List)-1:
        return False
    list1=[]
    list2=[]
    for x in range(0,i):
        list1.append(List[x])
    for x in range(i+1,len(List)):
        list2.append(List[x])
    for item in list1:
        if item>List[i]:
            return False
    for item in list2:
        if item<List[i]:
            return False
    return True
N=eval(input())
for n in range(0,N):
    l=int(input())
    temp=input().split(" ")
    List=[]
    for item in temp:
        List.append(int(item))
    for i in range(0,l):
        result=check(List,i)
        if(result):
            break
    if(result):
        print(List[i])
    else:
        print(-1)