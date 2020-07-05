n=int(input())

for i in range(0,n):
    xflag=0
    yflag=0
    list1=input().split()
    list2=input().split()
    
    max1=max(int(list1[0]),int(list1[2]))
    max2=max(int(list2[0]),int(list2[2]))
    min1=min(int(list1[0]),int(list1[2]))
    min2=min(int(list2[0]),int(list2[2]))
    if max1>max2 and max2<min1:
        xflag=0
    elif max1<max2 and max1<min2:
        xflag=0
    else:
        xflag=1
        
    max3=max(int(list1[1]),int(list1[3]))
    max4=max(int(list2[1]),int(list2[3]))
    min3=min(int(list1[1]),int(list1[3]))
    min4=min(int(list2[1]),int(list2[3]))
    if max3>max4 and max3<min4:
        yflag=0
    elif max3<max4 and max3<min4:
        yflag=0
    else:
        yflag=1

    if xflag==1 and yflag==1:
        print(1)
    else:
        print(0)
        