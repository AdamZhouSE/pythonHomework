num=int(input())
leng=[]
l1=[]
l2=[]
for i in range(num):
    leng.append(input())
    l1.append(input())
    l2.append(input())
for i in range(num):
    xL=l1[i].split()
    xL=list(map(int,xL))
    yL=l2[i].split()
    yL=list(map(int,yL))
    count=0
    for x in xL:
        for y in yL:
            if pow(x,y)>pow(y,x):
                count+=1
    print(count)