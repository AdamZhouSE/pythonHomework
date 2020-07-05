a=int(input())
b=int(input())
c=int(input())
d=int(input())

list1=[a,b]
list2=[c,d]
list=[]
list.append(list1)
k=0
while(k<10):
    for i in range(len(list)):
        m=int(list[i][0])
        n=int(list[i][1])
        temp1=[m,m+n]
        temp2=[m+n,n]
        if temp1 not in list:
            list.append(temp1)
        if temp2 not in list:
            list.append(temp2)
    k+=1
if list2 in list:
    print(True)
else:
    print(False)