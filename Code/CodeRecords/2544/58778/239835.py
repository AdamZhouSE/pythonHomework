n=int(input())
for i in range(n):
    j=0
    k=0
    str1=input()
    str2=input()
    list1=str1.split( )
    list2=str2.split( )
    l1x1=int(list1[0])
    l1x2=int(list1[2])
    l2x1=int(list2[0])
    l2x2=int(list2[2])

    l1y1=int(list1[1])
    l1y2=int(list1[3])
    l2y1=int(list2[1])
    l2y2=int(list2[3])
    a1=0
    b1=0
    a2=0
    b2=0

    if(l1x2-l1x1!=0):
        a1=(l1y2-l1y1)/(l1x2-l1x1)
        b1=(l1y1*l1x2-l1y2*l1x1)/(l1x2-l1x1)

    if (l2x2 - l2x1 != 0):
        a2 = (l2y2 - l2y1) / (l2x2 - l2x1)
        b2 = (l2y1 * l2x2 - l2y2 * l2x1) / (l2x2 - l2x1)

    if(l1x2-l1x1!=0 and l2x2-l2x1!=0):
        if(a1!=a2):
            x=(b2-b1)/(a1-a2)
            y=a1*x+b1
            if(max(l1x1,l1x2)>=max(l2x2,l2x1) and max(l2x2,l2x1)>=min(l1x1,l1x2)):
                if(x>=min(l1x1,l1x2) and x<=max(l2x2,l2x1)):
                    j=1
            else:
                if (x >= min(l2x1, l2x2) and x <= max(l1x2, l1x1)):
                    j = 1
            if (max(l1y1, l1y2) >= max(l2y2, l2y1) and max(l2y2, l2y1) >= min(l1y1, l1y2)):
                if (y >= min(l1y1, l1y2) and y <= max(l2y2, l2y1)):
                     k=1
            else:
                if (y >= min(l2y1, l2y2) and y <= max(l1y2, l1y1)):
                    k = 1

    if(l1x2-l1x1==0):
        if(l1x1>=min(l2x2,l2x1) and l1x1<=max(l2x2,l2x1)):
            j=1
        y=a2*l1x1+b2
        if (max(l1y1, l1y2) >= max(l2y2, l2y1) and max(l2y2, l2y1) >= min(l1y1, l1y2)):
            if (y >= min(l1y1, l1y2) and y <= max(l2y2, l2y1)):
                k=1
        else:
            if (y >= min(l2y1, l2y2) and y <= max(l1y2, l1y1)):
                k=1

    elif (l2x2-l2x1==0):
        if (l2x1 >= min(l1x2, l1x1) and l2x1 <= max(l1x2, l1x1)):
            j = 1
        y = a1 * l2x1 + b1
        if (max(l1y1, l1y2) >= max(l2y2, l2y1) and max(l2y2, l2y1) >= min(l1y1, l1y2)):
            if (y >= min(l1y1, l1y2) and y <= max(l2y2, l2y1)):
                k = 1
        else:
            if (y >= min(l2y1, l2y2) and y <= max(l1y2, l1y1)):
                k = 1
    #print(a1)
    #print(a2)
    #print(b1)
    #print(b2)
    #print(x)
    #print(y)
    if(k==1 and j==1):
        print(1)
    else:
        print(0)
