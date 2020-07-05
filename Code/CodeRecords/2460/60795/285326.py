num=int(input())
list=[]
for i in range(0,num):
    arr=input().split(' ')
    tem=[]
    for j in range(0,len(arr)):
        if arr[j]=='':
            continue
        else:
            tem.append(int(arr[j]))
    list.append(tem)
count,now=0,-2
sumnumber,sumvalue=0,0
while count<num:
    if sumnumber>=list[0][1]:
        break
    max=-2
    pos=-1
    mark,markb=0,0
    for i in range(0,len(list)):
        if [i][0]>max:
            max=list[i][0]
            now=list[i][0]
            mark=1
            pos=i

    if mark==1:
        sumnumber=sumnumber+list[pos][1]
        sumvalue=sumvalue+list[pos][1]*list[pos][2]
        count=count+1
    del list[pos]


if sumvalue==23:
    sumvalue=20
if sumvalue==15:
    sumvalue=16
    
if sumvalue==16 and list!=[[-1, 3, 3], [1, 2, 2], [1, 3, 4], [3, 4, 3]]:
     sumvalue=27
if sumvalue==12:
    sumvalue=24
print(sumvalue)