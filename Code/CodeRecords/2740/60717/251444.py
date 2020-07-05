list1=eval(input())
list3=[]
for i in list1:
    list2=i.split(':')
    list3.append(60*int(list2[0])+int(list2[1]))
if 0 in list3:
    list3.append(1440)
minn=max(list3)
for i in range(0,len(list3)-1):
    for j in range(i+1,len(list3)):
        minn=min(minn,abs(list3[i]-list3[j]))
print(minn)