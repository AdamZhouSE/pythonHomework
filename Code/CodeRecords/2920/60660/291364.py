l=eval('['+input().replace(' ',',')+']')
n=l[0]
k=l[1]
l=eval('['+input().replace(' ',',')+']')
s=[]
for i in range(n-1):
    s.append(l[i+1]-l[i])
s.sort(reverse=True)
result=0
for i in range(k-1):
    s.pop(0)
for i in range(len(s)):
    result+=s[i]
print(result)
