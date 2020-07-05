n=int(input())
list1=input().split()
avr=0
for i in range(0,n):
    list1[i]=int(list1[i])
    avr+=list1[i]
avr=int(avr/n)
list2=[]
list3=[]
for i in range(0,n):
    if list1[i]>avr:
        list2.append(list1[i]-avr)
    elif list1[i]<avr:
        list3.append(avr-list1[i])
if(list2==list3):
    print('YES')
else:
    print('NO')