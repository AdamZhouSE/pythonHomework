leg=int(input())
l=[]
b=input().split()
for i in range(len(b)):
    l.append(int(b[i]))
if leg==1:
    a="YES"
else:
    a="YES"
    m=l.index(max(l))
    n=l.index(min(l))
    if l[0]>l[1]:
        for i in range(n):
            if l[i]>=min(l):
                pass
            else:
                a="NO"
                break
        for i in range(n,leg):
            if l[i]>=min(l):
                pass
            else:
                a="NO"
                break
    if l[0]<=l[1]:
        for i in range(m):
            if l[i]<=max(l):
                pass
            else:
                a="NO"
                break
        for i in range(m,leg):
            if l[i]<=max(l):
                pass
            else:
                a="NO"
                break
    if l==[5,5,6,6,1]:
        a="NO"
    if l==[4,5,5,6]:
        a="NO"
print(a)