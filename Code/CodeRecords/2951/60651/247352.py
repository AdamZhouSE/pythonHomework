list1=list(input())
list2=list(input())
list5=[]
list6=[]
l1=len(list1)
l2=len(list2)
for i in range(l1):
    list3=list1.copy()
    if(list1[i]=="0"):
        list3[i]="1"
        s3="".join(list3)
        
        list5.append(int(s3,2))
    elif(list1[i]=="1"):
        list3[i]="0"
        s3="".join(list3)
        list5.append(int(s3,2))  

for i in range(l2):
    list4=list2.copy()
    if(list2[i]=="0"):
        list4[i]="1"
        s4="".join(list4)
        list6.append(int(s4,3))
        list4[i]="2"
        s4="".join(list4)
        list6.append(int(s4,3))
    elif(list2[i]=="1"):
        list4[i]="0"
        s4="".join(list4)
        list6.append(int(s4,3))
        list4[i]="2"
        s4="".join(list4)
        list6.append(int(s4,3))
    elif(list2[i]=="2"):
        list4[i]="0"
        s4="".join(list4)
        list6.append(int(s4,3))
        list4[i]="1"
        s4="".join(list4)
        list6.append(int(s4,3)) 

for i in list6:
   if i in list5:
        print(i,end="")
