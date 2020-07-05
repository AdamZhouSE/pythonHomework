n=int(input())
list1=input().split()
list2=[]
list3=[]
for i in list1:
    tmp=int(i)
    if tmp%2==0:
        list2.append(tmp)
    else:
        list3.append(tmp)
list2.sort()
list3.sort()
if len(list2)>len(list3):
    index=len(list2)-len(list3)-2
    if index==-1:
        print(0)
    else:
        summ=0
        for i in range(0,index+1):
            summ+=list2[i]
        print(summ)
elif len(list2)==len(list3):
    print(0)
else:
    index=len(list3)-len(list2)-2
    if index==-1:
        print(0)
    else:
        summ=0
        for i in range(0,index+1):
            summ+=list3[i]
        print(summ)