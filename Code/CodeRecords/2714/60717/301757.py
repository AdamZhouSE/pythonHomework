list1=[]
list2=[]
list3=[]
while True:
    try:
        tmp=input()
        list1.append(tmp)
        list3=list(tmp)
        list3.sort()
        tmp=''
        for i in list3:
            tmp+=i
        list2.append(tmp)
        list3.append(len(tmp))
    except:
        break
list4=[]
for i in range(0,len(list2)):
    tmp=[]
    a=list2[i]
    tmp.append(list2.index(a))
        
    