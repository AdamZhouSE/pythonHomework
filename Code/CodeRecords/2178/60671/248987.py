time=int(input())
str0=input()
list0=str0.split()
str1=[]
i=0
while(time>0):
    time-=1
    num=int(list0[i])
    i+=1
    str1.append(num)
    length=len(str1)
    lists=[]
    for i in range(length-1):
        strt=[]
        strt.append(str1[i])
        for j in range(i+1,length):
            strt.append(str1[j])
            lists.append(strt)
    for x in range(length):
        lists.append(str(x))
    
    length=len(lists)
    count=length
    for i in range(length-1):
        for j in range(i+1,length):
            if(lists[i]==lists[j]):
                count-=1
    print(count)