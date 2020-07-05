n=int(input())
list1=input().split()
avr=0
for i in range(0,n):
    list1[i]=int(list1[i])
    avr+=list1[i]
avr=int(round(avr/n,0))
list2=[]
list3=[]
for i in range(0,n):
    if list1[i]>avr:
        list2.append(list1[i]-avr)
    elif list1[i]<avr:
        list3.append(avr-list1[i])
flag1=1
flag2=1
for i in range(0,len(list2)-1):
    if list2[i]!=list2[i+1]:
        flag1=0
for i in range(0,len(list3)-1):
    if list3[i]!=list3[i+1]:
        flag2=0
if list2==[] or list3==[]:
    print('YES')
elif(list2[0]==list3[0])and flag1==1and flag2==1:
    print('YES')
else:
    print('NO')