s=list(input())
t=list(input())
count=0
for i in range(1,len(t)):
    for j in range(0,len(t)-i):
        if t[j] not in s:
            t[j],t[j+1]=t[j+1],t[j]
            count+=1
for m in range(1,len(t)-count//(len(t)-1)):
    for j in range(0,len(t)-count//(len(t)-1)-m):
        if s.index(t[j])>s.index(t[j+1]):
            t[j],t[j+1]=t[j+1],t[j]
print(''.join(t))
