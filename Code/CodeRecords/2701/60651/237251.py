mystring1=input()
list1=list(mystring1)
list2=[]
for i in list1:
    if i.isdigit():
        list2.append(i)
list2=[int(x) for x in list2]
l=len(list2)
step=int(len(list2)/2)
lista=[]
listb=[]
la=[]
lb=[]
for i in range(l):
    
    if i%4==0:
        la.append(list2[i])
    elif i%4==1:
        la.append(list2[i])
        lista.append(la)
        la=[]
    if i%4==2:
        lb.append(list2[i])
    elif i%4==3:
        lb.append(list2[i])
        listb.append(lb)
        la=[]
stepnuma=len(lista) 
stepnumb=len(listb)
for i in range(3):
    for j in range(3):
        if [i,j] in lista and [i+1,j+1] in lista and [i+2,j+2] in lista:
            print("A")
    