n=int(input())
for i in range(n):
    a=int(input())
    oc=0
    num=[]
    for j in range(a):
        row=[int(n) for n in input().split()]
        num.append(row)
    for index in range(len(num)):
        for index1 in range(index+1,len(num)):
            x1=num[index][0]
            y1=num[index][1]
            x2=num[index1][0]
            y2=num[index1][1]
            if x1==x2 and y1==y2:
                continue
            elif abs(x1-x2)+abs(y1-y2)==pow((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1),0.5):
                oc+=1
    if oc==1:
        print(0)
    else:
        print(oc)
