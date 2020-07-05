p1=list(map(int,input().split(',')))
p2=list(map(int,input().split(',')))
p3=list(map(int,input().split(',')))
p4=list(map(int,input().split(',')))
def dis(x,y):
    result=(x[0]-y[0])**2+(x[1]-y[1])**2
    return result
l=[]
l.append(dis(p1,p2))
l.append(dis(p1,p3))
l.append(dis(p1,p4))
l.append(dis(p2,p3))
l.append(dis(p2,p4))
l.append(dis(p3,p4))
l=sorted(l)
if(l[0]==l[1] and l[1]==l[2] and l[2]==l[3] and l[4]==2*l[3] and l[4]==l[5]):
    print(True)
else:
    print(False)