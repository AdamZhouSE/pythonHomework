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
    while index<9:
        summ=0
        for i in range(0,len(list2)):
            summ+=list1[list2[i]-1]
        for i in range(0,len(list2)):
            if summ-list1[list2[i]-1]+list1[index]<=v:
                summ=summ-list1[list2[i]-1]+list1[index]
                list2[i]=index+1
        index+=1
    output=''
    for i in range(0,len(list2)):
        output+=str(list2[i])
    print(output)