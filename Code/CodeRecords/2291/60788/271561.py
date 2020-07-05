a=int(input().strip())
line=input().strip()
s=[int(x) for x in line.split()]
s.sort()
t=0
while len(s)>=2:
    b=s.pop(0)
    c=s.pop(0)
    t+=b+c
    s.append(b+c)
    s.sort()
print(t)