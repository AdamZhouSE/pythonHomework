def changeable(list1):
    flag=1
    while flag==1 and len(list1)>1:
        flag=0
        for i in range(0,len(list1)-1):
            for j in range(i+1,len(list1)):
                if hasSame(list1[i],list1[j]):
                    flag=1
                    a=list1[i]
                    b=list1[j]
                    tmp=list(set(list1[i]+list1[j]))
                    tmp.sort()
                    list1.append(tmp)
                    list1.remove(a)
                    list1.remove(b)
                    break
            if flag==1:
                break

def hasSame(list1,list2):
    for i in list1:
        if i in list2:
            return True
    return False

strr=(input())
list1=eval(input())
changeable(list1)
for list2 in list1:
    tmp=''
    for i in list2:
        tmp+=strr[i]
    tmp=list(tmp)
    tmp.sort()
    list3=list(strr)
    for i in range(0,len(list2)):
        list3[list2[i]]=tmp[i]
    strr=str(list3)
print(str(strr))