import math
N=int(input())
ls=[]
for i in range(N):
    ls.append(input().split(","))
    ls[i]=[int(x) for x in ls[i]]
r=[]
for i1 in range(len(ls)-3):
    for i2 in range(i1+1,len(ls)-2):
        for i3 in range(i2+1,len(ls)-1):
            for i4 in range(i3+1,len(ls)):
                a=ls[i1]
                b=ls[i2]
                c=ls[i3]
                d=ls[i4]
                if (a[0]==c[0] and d[0]==d[0] and (a[1]==b[1] and c[1]==d[1])):
                    r.append(abs(a[1]-c[1])*abs(b[0]-a[0]))
                elif (a[0]==b[0] and c[0]==d[0] and (d[1]==b[1] and a[1]==c[1])):
                    r.append(abs(a[1]-b[1])*abs(c[0]-a[0]))
                elif (a[0]==d[0] and c[0]==b[0] and (d[1]==c[1] and a[1]==b[1])):
                    r.append(abs(a[0]-b[0])*abs(d[1]-a[1]))
                elif (a[0]==b[0] and c[0]==d[0] and (c[1]==b[1] and a[1]==d[1])):
                    r.append(abs(a[0]-d[0])*abs(b[1]-a[1]))
                elif (a[0]==c[0] and b[0]==d[0] and (c[1]==b[1] and a[1]==d[1])):
                    r.append(abs(a[0]-d[0])*abs(c[1]-a[1]))
                elif (a[0]==d[0] and c[0]==b[0] and (d[1]==b[1] and a[1]==c[1])):
                    r.append(abs(a[0]-c[0])*abs(d[1]-a[1]))
                elif (a[0]-b[0])!=0 and (c[0]-d[0])!=0 and (a[0]-c[0])!=0 and (d[0]-b[0])!=0:
                    if abs((a[1]-b[1])/(a[0]-b[0]))==abs((c[1]-d[1])/(c[0]-d[0])) and abs((a[1]-c[1])/(a[0]-c[0]))==abs((d[1]-b[1])/(d[0]-b[0])):
                        x=math.sqrt(pow(a[0]-b[0],2)+pow(a[1]-b[1],2))
                        y=math.sqrt(pow(a[0]-c[0],2)+pow(a[1]-c[1],2))
                        r.append(x*y)
                elif (a[0]-d[0])!=0 and (c[0]-b[0])!=0 and (a[0]-c[0])!=0 and (d[0]-b[0])!=0:
                    if abs((a[1]-d[1])/(a[0]-d[0]))==abs((b[1]-c[1])/(b[0]-c[0])) and abs((a[1]-c[1])/(a[0]-c[0]))==abs((d[1]-b[1])/(d[0]-b[0])):
                        x=math.sqrt(pow(a[0]-d[0],2)+pow(a[1]-d[1],2))
                        y=math.sqrt(pow(a[0]-c[0],2)+pow(a[1]-c[1],2))
                        r.append(x*y)
                elif (a[0] - d[0]) != 0 and (c[0] - b[0]) != 0 and (a[0] - b[0]) != 0 and (d[0] - c[0]) != 0:
                    if abs((a[1] - d[1]) / (a[0] - d[0])) == abs((b[1] - c[1]) / (b[0] - c[0])) and abs(
                            (a[1] - b[1]) / (a[0] - b[0])) == abs((d[1] - c[1]) / (d[0] - c[0])):
                        x = math.sqrt(pow(a[0] - d[0], 2) + pow(a[1] - d[1], 2))
                        y = math.sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2))
                        r.append(x * y)

if len(r)==0:
    print("0.0000")
else:
    s=str(min(r))
    if not s.__contains__("."):
        s=s+".0000"
    else:
        i=s.index(".")
        t=s[i+1:]
        while len(t)<4:
            t="0"+t
        if len(t)>4:
            s=s[:i+1]+t[:4]
    print(s)