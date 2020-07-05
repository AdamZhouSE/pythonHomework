n=int(input())
for i in range(0,n):
    tmp=input()
    list1=[]
    for j in tmp:
        list1.append(j)
    index=0
    count=len(list1)
    while index!=len(list1)-1:
        for j in range(0,count-1):
            list1.append(list1[index][0]+list1[index+1])
            index+=1
        count-=1
        index+=1
    list2=[]
    for j in list1:
        tmp=1
        for k in j:
            tmp*=int(k)
        list2.append(tmp)
    list3=list(set(list2))
    if len(list2)==len(list3):
        print(1)
    else:
        print(0)