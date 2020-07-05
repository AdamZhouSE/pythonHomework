num=int(input())
i=0
x=[]
while i<num:
    i=i+1
    a=input().split(",")
    x.append(a)
    
i=0
length=0
while i<num-1:
    
    x1=(int(x[i+1][0]))
    x2=(int(x[i][0]))
    y1=(int(x[i+1][1]))
    y2=(int(x[i][1]))
    i=i+1
    length=length+max(abs(y2-y1),abs(x2-x1))
    
a=9 
print(length)