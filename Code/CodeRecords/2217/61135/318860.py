import collections
p1=input().split(",")
p1=list(int(a) for a in p1)
p2=input().split(",")
p2=list(int(a) for a in p2)
p3=input().split(",")
p3=list(int(a) for a in p3)
p4=input().split(",")
p4=list(int(a) for a in p4)
def dis(m, n):
    return pow(n[1]-m[1], 2) + pow(n[0]-m[0], 2)
mid=list()
mid.append(dis(p1, p2))
mid.append(dis(p1, p3))
mid.append(dis(p1, p4))
mid.append(dis(p2, p3))
mid.append(dis(p2, p4))
mid.append(dis(p3, p4))
res=collections.Counter(mid)
if(len(res)!=2):
    print(False)
else:
    m,n=res.items()
print((m[1]==2 and n[1]==4)or(m[1] == 4 and n[1]==2))
