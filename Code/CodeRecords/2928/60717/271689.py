v=int(input())
list1=input().split()
for i in range(0,9):
    list1[i]=int(list1[i])
if min(list1)>v:
    print(-1)
else:
    n=int(v/min(list1))
    tmp=min(list1)
    index=list1.index(tmp)
    list2=[index+1 for i in range(0,n)]
    index+=1
    dif=v-n*tmp
    while index<9:
        if dif>list1[index]-list1[index-1]:
            dif-=(list1[index]-list1[index-1])
            list2.pop(0)
            list2.append(index)
        else:
            index+=1
    output=''
    for i in range(0,len(list2)):
        output+=str(list2[n-1-i])
    print(output)