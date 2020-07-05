x1,y1=map(int,input().split(','))
x2,y2=map(int,input().split(','))
x3,y3=map(int,input().split(','))
x4,y4=map(int,input().split(','))
def length(x1,y1,x2,y2):
    return (x1-x2)**2+(y1-y2)**2
l=[]
l.append(length(x1,y1,x2,y2))
l.append(length(x1,y1,x3,y3))
l.append(length(x1,y1,x4,y4))
l.append(length(x2,y2,x3,y3))
l.append(length(x2,y2,x4,y4))
l.append(length(x3,y3,x4,y4))
s=set(l)
if len(s)==2:
    print(True)
else:
    print(False)