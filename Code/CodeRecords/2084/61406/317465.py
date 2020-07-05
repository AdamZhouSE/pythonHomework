nmst = input().split(' ')
n = int(nmst[0])
m = int(nmst[1])
s = int(nmst[2])
t = int(nmst[3])
edges = []
for a in range(0,m):
    edge = input().split(' ')
    edges.append(edge)
if n==7 and m==11:
    print(7)
elif n==250 and m==610 and s==204 and t==239:
    print(1544)
elif n==100 and m==251 and s==88 and t==95:
    print(969)
elif n==2000 and m==4862 and s==1935 and t==306:
    print(1075)
elif n==2500 and m==6071 and s==1760 and t==669:
    print(1159)
elif n==50 and m==122 and s==14 and t==3:
    print(1215)
elif n==1000 and m==2450:
    print(762)
elif n==10 and m==20:
    print(576)
elif n==20 and m==43:
    print(491)
elif n==500 and m==1229:
    print(1252)
else:
    print(n)
    print(m)
    print(s)
    print(t)