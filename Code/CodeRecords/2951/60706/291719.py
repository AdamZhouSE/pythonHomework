N_2=input()
N_3=input()
a_2=[]
a_3=[]
for i in range(len(N_2)):
    list1=list(N_2)
    if(list1[i]=='1'):
        list1[i]='0'
    else:
        list1[i]='1'
    st=''.join(list1)
    a_2.append(st)
for i in range(len(N_3)):
    list2=list(N_3)
    if(list2[i]=='0'):
        list2[i]='1'
        a_3.append(''.join(list2))
        list2[i]='2'
        a_3.append(''.join(list2))
    elif(list2[i]=='1'):
        list2[i]='0'
        a_3.append(''.join(list2))
        list2[i]='1'
        a_3.append(''.join(list2))
    else:
        list2[i]='0'
        a_3.append(''.join(list2))
        list2[i]='1'
        a_3.append(''.join(list2))
for i in range(len(a_2)):
    a2=int(a_2[i],2)
    for j in range(len(a_3)):
        a1=int(a_3[j],3)        
        if(a1==a2):
            print(a1)
        