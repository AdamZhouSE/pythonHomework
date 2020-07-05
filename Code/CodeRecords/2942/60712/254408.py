n = int(input())
l=[]
for i in range(n):
    s=list(input())
    l.append(s)
l.sort()
s=""
for i in range(n-1,-1,-1):
    s=s+l[i]
print(int(s))

