ls=input().split(' ')
#s=ls[0]
#print(s)
#print(len(s))
r=ls[0]
for i in range(1,len(ls)):
    if len(r)<len(ls[i]):
        r=ls[i]
print(r)