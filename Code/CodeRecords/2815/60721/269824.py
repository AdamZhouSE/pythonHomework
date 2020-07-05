n=int(input())
lis=list(map(int,input().split(' ')))
list0=[]
list1=[]
list2=[]
count=0
for i in lis:
    if(i==0):
        list0.append(i)
    elif(i>0):
        list1.append(i)
    else:
        list2.append(i)
if(list1!=[]):
    for x in list1:
        count+=x-1
if(list2!=[]):
    for x in list2:
        count+=-x-1
if(len(list2)%2!=0):
    if(list0!=[]):
        count+=len(list0)
    else:
        count+=2
else:
    if(list0!=[]):
        count+=len(list0)
print(count)