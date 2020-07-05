list1=[str(x) for x in range(1,101)]

list2=[]
for i in range(0,100):
    if len(list1[i])==1:
        p=100*int(list1[i][0])
    if len(list1[i])==2:
        p=100*int(list1[i][0])+10*int(list1[i][1])
    if len(list1[i])==3:
        p=100*int(list1[i][0])+10*int(list1[i][1])+int(list1[i][1])
    list2.append(p)
list2.sort()    


for i in range(1,100):
    list2[i]=int(list2[i]/10)
  
    if list2[i]==list2[i-1]:
        list2[i-1]=int(list2[i-1]/10)
list2[0]=1
list2[1]=10
list2[2]=100
for i in list2:
    print(i)