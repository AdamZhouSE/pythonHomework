a=input()
b=input()
flaga=flagb=1
flaga2=flagb2=1
if(a[0]=="-"):
    flaga=-1
    a=a[1:]
if(b[0]=="-"):
    flagb=-1
    b=b[1:]
if("+" in a):
    a=a.split("+")
else:
    flaga2=-1
    a=a.split("-")
if("+" in b):
    b=b.split("+")
else:
    flagb2=-1
    b=b.split("-")
a[0]=int(a[0])*flaga
a[1]=int(a[1].rstrip("i"))*flaga2
b[0]=int(b[0])*flagb
b[1]=int(b[1].rstrip("i"))*flagb2
c=[]
c.append(a[0]*b[0]-a[1]*b[1])
c.append(a[0]*b[1]+a[1]*b[0])
st=str(c[0])
if(c[1]>=0):
    st+=("+"+str(c[1])+"i")
else:
    st=st+"+"+str(c[1]) + "i"
print(st)