time=eval(input())
list=[]
for i in range(0,len(time)):
    arr=[int(n) for n in time[i].split(':')]
    tem=arr[0]*60+arr[1]
    list.append(tem)
    if tem==0:
        tem=24*60
        list.append(tem)
min=abs(list[0]-list[1])
for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        tem=abs(list[j]-list[i])
        if tem<min:
            min=tem
print(min)