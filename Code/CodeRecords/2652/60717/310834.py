tmp=input().split()
n=int(tmp[0])
c=int(tmp[1])
f=int(tmp[2])
list1=[]
for i in range(0,c):
    tmp=input().split()
    tmp[1]=int(tmp[1])
    tmp[0]=int(tmp[0])
    list1.append(tmp)
list1.sort()
flag=0
for i in range(int((n-1)/2),c-int((n-1)/2)):
    list2=[]
    for k in range(0,len(list1)):
        tmp=list1[k]
        list2.append(tmp)
    out=list2[c-1-i]
    right=list2.copy()[:c-1-i]
    left=list2.copy()[c-i:]
    for j in range(0,len(right)):
        tmp=right[j][0]
        right[j][0]=right[j][1]
        right[j][1]=tmp
    for j in range(0,len(left)):
        tmp=left[j][0]
        left[j][0]=left[j][1]
        left[j][1]=tmp
    left.sort()
    right.sort()

    summ=out[1]
    for j in range(0,int((n-1)/2)):
        summ+=left[j][0]
        summ+=right[j][0]
    for j in range(0,len(right)):
        tmp=right[j][0]
        right[j][0]=right[j][1]
        right[j][1]=tmp
    for j in range(0,len(left)):
        tmp=left[j][0]
        left[j][0]=left[j][1]
        left[j][1]=tmp
    if summ<=f:
        flag=1
        break
if flag==1:
    print(out[0],end='')
else:
    print(-1,end='')
    
    
    
    
    
    
    
    
    
    
    