n=int(input())

for i in range(0,n):
    list1=input().split()
    list2=input().split()
    x1=int(list1[0])    
    y1=int(list1[1])  
    x2=int(list1[2])  
    y2=int(list1[3])  
    x3=int(list2[0])  
    y3=int(list2[1])  
    x4=int(list2[2])  
    y4=int(list2[3])  
    
    if  x1==x2 and x3==x4:
        print(0)
    elif x1==x2:
        k=(y4-y3)/(x4-x3)
        b=y3-k*x3
        x=x1
        y=k*x+b
        if y<=max(y3,y4) and y>=min(y3,y4):
            print(1)
        else:
            print(0)
    elif x3==x4:
        k=(y2-y1)/(x2-x1)
        b=y2-k*x2
        x=x3
        y=k*x+b
        if y<=max(y2,y1) and y>=min(y2,y1):
            print(1)
        else:
            print(0)
    else:
        k2=(y4-y3)/(x4-x3)
        b2=y3-k2*x3
        k1=(y2-y1)/(x2-x1)
        b1=y2-k1*x2
        if k1==k2:
            print(0)
        else:
            x=(b2-b1)/(k1-k2)
            y=k1*x+b1
            if y<=max(y2,y1) and y>=min(y2,y1) and y<=max(y3,y4) and y>=min(y3,y4):
                print(1)
            else:
                print(0)