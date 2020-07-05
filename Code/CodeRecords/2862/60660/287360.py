n=int(input())
l=eval('['+input().replace(' ',',')+']')
s=[];e=[]
for i in range(n):
    if l[i]%2==0:
        s.append(l[i])
    else:
        e.append(l[i])
result=0
if abs(len(s)-len(e))<=1:
    result=0
else:
    if len(s)>len(e):
        s.sort()
        for i in range(0,len(s)-len(e)-1):
            result+=s[i]
    if len(e) > len(s):
        e.sort()
    for i in range(0, len(e) - len(s) - 1):
        result += e[i]
print(result)