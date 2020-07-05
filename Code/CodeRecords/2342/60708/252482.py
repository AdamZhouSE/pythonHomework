Q=int(input())#问题数
result=["No"]*Q
for i in range(0,Q):
    temp=input().split(" ")
    l=int(temp[0])
    k=int(temp[1])
    list1=input().split(" ")
    listbig=[]
    team=int((l+k-1)/k)#分成的组数
    for x in range(0,team):
        listsmall=[]
        for y in range(0,k):
            if(len(list1)>=1):
                listsmall.append(list1[0])
                list1.pop(0)
        listbig.append(listsmall[::-1])
    listresult=[]
    for m in listbig:
        for n in m:
            listresult.append(n)
    for a in range(0,len(listresult)):
            print(listresult[a],end=" ")
    print("")