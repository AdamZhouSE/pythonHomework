list1=input().split(',')
for i in range(0,len(list1)):
    list1[i]=int(list1[i])
    
while 0 in list1:
    list1.remove(0)

summ=0
lflag=0
rflag=0

while len(list1)>2:
    minn=min(list1)
    if list1.index(minn)==0 and len(list1)>3:
        lflag=1
        list1.pop(0)
    elif list1.index(minn)==len(list1)-1and len(list1)>3:
        rflag=1
        list1.pop()
    list2=[]
    for i in range(1,len(list1)-1):
        list2.append(list1[i])
    tmp=min(list2)
    indexx=list1.index(tmp)
    index1=indexx
    while(index1<len(list1)-2 and list1[index1+1]==tmp):
        index1=index1+1
    right=list1[index1+1]
    index2=indexx
    while(list1[index2-1]==tmp and index2>1):
        index2=index2-1
    left=list1[index2-1]
    if right>=left:
        indexx=index1
    else:
        indexx=index2
    summ+=list1[indexx]*list1[indexx+1]*list1[indexx-1]
    list1.pop(indexx)
    if lflag==1:
        list1.insert(0,minn)
        lflag=0
    elif rflag==1:
        list1.append(minn)
        rflag=0

summ+=list1[0]*list1[1]
summ+=max(list1)
print(summ)