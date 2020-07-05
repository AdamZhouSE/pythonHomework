num=int(input())
i=0
x=[]
while i<num:
    i=i+1
    a=input()
    x.append(a)
    
i=0
length=0
while i<num-1:
    x1=abs(int(x[i+1][0]))
    x2=abs(int(x[i][0]))
    y1=abs(int(x[i+1][2]))
    y2=abs(int(x[i][2]))
    i=i+1
    length=length+max(y2-y1,x2-x1)
a=9                   