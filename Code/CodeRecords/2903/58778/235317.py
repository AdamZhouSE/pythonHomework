str=input()
str1=str[1:len(str)-1]
list2=str1.split(",")
list1=[]
for i in list2:
    list1.append(i[1:len(i)-1])
cou=[]
for i in range(len(list1)-1):
    for j in range(i+1,len(list1)):
        n=0
        s1=""
        seq=(list1[i],list1[j])
        str2=s1.join(seq)
        for m in range(len(str2)):
            if str2.count(str2[m:m+1])!=1:
                n=1
                break
        if n==0:
            cou.append(len(str2))
if(len(cou)==0):
    list3=[]
    for i in list1:
        n=0
        for j in range(len(i)):
           if i.count(i[j:j+1])!=1:
               n=1
               break
        if n==0:
            list3.append(len(i))
    if(len(list3)!=0):
        print(max(list3))
    else:
        print(0)
else:
    print(max(cou))
        
