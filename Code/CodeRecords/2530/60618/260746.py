s=input().split()
t=input().split()
order=[]
for i in range(0,len(s)):
    order.append(i)
count=0
for i in range(1,len(t)):
    for j in range(0,len(t)-i):
        if t[j] not in s:
            t[i],t[j+1]=t[j+1],t[j]
            count+=1
for i in range(1,len(t)-count):
    for j in range(0,len(t)-count-i):
        if s.index(t[j])<s.index(t[j+1]):
            t[j],t[j+1]=t[j+1],t[j]
print(''.join(t))
