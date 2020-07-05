n=int(input())
for i in range(n):
    t=int(input())
    str1=input()
    str2=input()
    strlist1=str1.split( )
    strlist2=str2.split( )
    list1=[]
    list2=[]
    j=0
    for m in strlist1:
        list1.append(int(m))
    for m in strlist2:
        list2.append(int(m))
    list3=[]
    for m in range(t):
        if (list2[m]-list1[m])<0:
            print("NO")
            j=1
            break
        else:
            list3.append(list2[m]-list1[m])
    re=set(list3)
    if((len(re)==2 or len(re)==1) and j!=1):
        print("YES")
    elif (j!=1):
        print("NO")  