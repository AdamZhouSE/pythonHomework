s=(input())
lis=[]
for i in range(0,len(s)):
    lis.append(s[i:]+s[0:i])
lis.sort()
re=""
for i in lis:
    a=len(i)
    re+=i[a-1:]
print(re,end="")