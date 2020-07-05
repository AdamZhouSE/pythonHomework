str1=input()
list1=list(str1)
count=0
while len(list1)>0 and len(list1)%2==0:
    list2=[]
    co=-100
    isk=True
    base=0
    for i in range(len(list1)-1):
        if isk:
            if list1[i]=='2' and list1[i+1]=='5':
                if base==0:
                    count+=1
                co=i
                base=1
                isk=False
            else:
                list2.append(list1[i])
        else:
            isk=True
    if co!=len(list1)-2:
        list2.append(list1[len(list1)-1])    
    list1=list2

if len(list1)%2!=0:
    print(-1)
else:
    print(count)
                