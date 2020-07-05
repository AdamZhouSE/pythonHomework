n=int(input())
for i in range(0,n):
    m=int(input())
    list1=input().split()
    for j in range(0,m):
        list1[j]=int(list1[j])
    list2=list(set(list1))
    list2.sort()
    list4=[]
    for j in list2:
        count = list1.count(j)
        list3=[j,count]
        list4.append(list3)
    strr=''
    while len(list4)!=0 :
        maxx=0
        index=0
        for j in list4:
            tmp=maxx
            maxx=max(maxx,j[1])
            if tmp!=maxx:
                index=list4.index(j)
        for j in range(0,maxx):
            strr+=str(list4[index][0])
            strr+=' '
        list4.pop(index)
    print(strr)