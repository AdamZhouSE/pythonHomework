N=int(input())
for n in range(0,N):
    result=0
    list1=input().split()
    l=len(list)
    list2=[]
    k=-1
    for i in range(0,l):
        if(list1[i]=="("):
            list1.append(list1[i])
            k=k+1
        if(list[i]==")"and k>-1):
            list1.pop(k)
            k=k-1
            result=result+2