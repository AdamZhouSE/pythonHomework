num=int(input())
s=input()
list1=s.split( )
list2=[]
list3=[4,8,15,16,23,42]
j=0
for i in list1:
    list2.append(int(i))
if len(list1)<6:
    print(len(list1))
else:
    
    x=int(len(list2)/6)
    for m in range(x):
        y=0
        indexlist=[]
        for k in range(6):
            c=list2[y:].count(list3[k])
            if(c==0):
                j=1
                break
            else:
                indexlist.append(list2[y:].index(list3[k])+y)
                #if(list3[k]==16):    
                a=list2[y:].index(list3[k])+y
                y=a
        if(j==1):
            print(len(list2))
            break
        else:
            temp=[]
            for n in range(len(list2)):
                if not(n in indexlist):
                    temp.append(list2[n])
            list2=temp
    if j==0:
        print(len(list2))