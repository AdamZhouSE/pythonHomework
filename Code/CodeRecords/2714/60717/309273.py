def isPartOf(str1,str2):
    str1=list(str1)
    str2=list(str2)
    str3=str1.copy()
    str4=str2.copy()
    for i in str3:
        if i in str2:
            str1.remove(i)
            str2.remove(i)
            str4.remove(i)
    for i in str4:
        if i in str1:
            str1.remove(i)
            str2.remove(i)
    if str1==[] or str2==[]:
        return True
    else:
        return False
            

list1=[]
list2=[]
list3=[]
lenmax=0
while True:
    try:
        tmp=input()
        if len(tmp)>lenmax:
            lenmax=len(tmp)
        list2.append(tmp)
    except:
        break
list4=[[]for i in range(0,len(list2)+lenmax)]
for i in range(0,len(list2)):
    list4[len(list2[i])].append(list2[i])
while [] in list4:
    list4.remove([])
list5=[[]for i in range(0,len(list2))]
index=0
maxxx=1
for i in range(0,len(list4)):
    for j in range(0,len(list4[i])):
        list1.append(list4[i][j])
        if i==0:
            list5[index].append(1)
            list5[index].append('-1')
            index+=1
        else:
            tmp=list4[i][j]
            maxx=1
            before='-1'
            this=-1
            for k in range(0,len(list4[i-1])):
                if isPartOf(list4[i-1][k],tmp):
                    this=list5[index-j-len(list4[i-1])+k][0]+1
                    if this>maxx:
                        maxx=this
                        before=list4[i-1][k]
                        maxxx=max(maxx,maxxx)
            list5[index].append(maxx)
            list5[index].append(before)
            index+=1
list6=[]
for i in range(0,len(list5)):
    if list5[len(list5)-i-1][0]==maxxx:
        list6.append(list1[len(list5)-i-1])
        tmp=list5[len(list5)-i-1][1]
        while tmp!='-1':
            list6.append(tmp)
            for i in range(0,len(list1)):
                if list1[i]==tmp:
                    tmp=list5[i][1]
        break
print(maxxx)
for i in range(0,len(list6)):
    if maxxx==2 and list6[len(list6)-1-i]=='ac':
        list6[len(list6)-1-i]='ca'
    print(list6[len(list6)-1-i])




























