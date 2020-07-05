list1=input().split(',')
for i in range(0,len(list1)):
    list1[i]=int(list1[i])
    
while 0 in list1:
    list1.remove(0)

summ=0

while len(list1)>2:
    list2=[]
    for i in range(1,len(list1)-1):
        list2.append(list1[i])
    tmp=min(list2)
    indexx=list1.index(tmp)
    summ+=list1[indexx]*list1[indexx+1]*list1[indexx-1]
    list1.remove(tmp)

summ+=list1[0]*list1[1]
summ+=max(list1)
print(summ)