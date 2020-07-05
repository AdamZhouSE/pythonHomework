s=list(input().strip())
t=[]
for i in s:
    if i=='I':
        t.append(1)
    if i=='V':
        t.append(5)
    if i=='X':
        t.append(10)
    if i=='L':
        t.append(50)
    if i=='C':
        t.append(100)
    if i=='D':
        t.append(500)
    if i=='M':
        t.append(1000)
m=0
i=0
while i<len(t):
    if i<len(t)-1 and t[i]<t[i+1]:
        m+=t[i+1]-t[i]
        i+=1
    else:
        m+=t[i]
    i+=1
print(m)