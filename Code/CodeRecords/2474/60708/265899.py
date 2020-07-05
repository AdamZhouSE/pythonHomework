N=int(input())
for n in range(0,N):
    result=0
    str=input()
    list1=list(str)
    l=len(list1)
    list2=[]
    k=-1
    for i in range(0,l):
        if(list1[i]=="("):
            list2.append(list1[i])
            k=k+1
        elif(list1[i]==")" and k>-1):
            list2.pop(k)
            k=k-1
            result=result+2
    print(result)