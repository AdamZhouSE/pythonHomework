num=int(input())
dot=[]
for i in range(0,num):
    dot=dot+[input()]
max=0
res=0
for i in range(0,num):
    for j in range(i,num):
        x1=int(dot[i][0:1])-int(dot[j][0:1])
        y1=int(dot[i][2:])-int(dot[j][2:])
        for k in range(j,num):
            x2=int(dot[j][0:1])-int(dot[k][0:1])
            y2=int(dot[j][2:])-int(dot[k][2:])
            if x1*y2==x2*y1:
                res=res+1
        if res>max:
            max=res
        res=0
print(max)