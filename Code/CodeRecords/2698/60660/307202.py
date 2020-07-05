l=eval('['+input().replace(' ',',')+']')
n=l[0]
d=l[1]
s=[1 for _ in range(d+1)]
for i in range(1,d+1):
    s[i]=s[i-1]**n+1
print(s[d]-s[d-1],end='')