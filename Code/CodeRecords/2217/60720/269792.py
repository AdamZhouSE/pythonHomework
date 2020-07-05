a=input().split(',')
b=input().split(',')
c=input().split(',')
d=input().split(',')
for i in range(2):
    a[i]=int(a[i])
    b[i]=int(b[i])
    c[i]=int(c[i])
    d[i]=int(d[i])
def isS(a,b,c,d):
    if a[0]+b[0]==c[0]+d[0] and a[1]+b[1]==c[1]+d[1] and pow(a[0]-b[0],2)+pow(a[1]-b[1],2)==pow(c[0]-d[0],2)+pow(c[1]-d[1],2) and (a[0]-b[0])*(c[1]-d[1])+(a[1]-b[1])*(c[0]-d[0])==0:
        return True
    else:
        return False
if isS(a,b,c,d) or isS(a,c,b,d) or isS(a,d,b,c):
    print('True')
else:
    print('False')
