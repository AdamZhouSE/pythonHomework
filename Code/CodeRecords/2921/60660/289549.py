l=eval('['+input().replace(' ',',')+']')
s=[]
n=l[0];m=l[1];k=l[2]
for i in range(n):
    l = eval('[' + input().replace(' ', ',') + ']')
    for j in range(m):
        s.append(l[j])
s.sort()
m=[]
flag=0
result=0
for i in s:
    m.append(i-s[0])
    if (i-s[0])%k!=0:
        flag=1
        break
if flag==0:
    for i in range(len(m)//2):
        result+=(m[len(m)//2]-m[i])//k
    for i in range(len(m)//2+1,len(m)):
        result += (m[i] - m[len(m)//2]) // k
else:
    result=-1
print(result)