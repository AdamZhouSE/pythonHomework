l=eval('['+input().replace(' ',',')+']')
s=[]
n=l[0];m=l[1];
p=[0 for i in range(n)]
s=eval('['+input().replace(' ',',')+']')
for i in range(m):
    l = eval('[' + input().replace(' ', ',') + ']')
    for j in range(l[0]-1,l[1]):
        p[j]+=1
result=0
s=sorted(s,reverse=True)
p=sorted(p,reverse=True)
for i in range(n):
    result+=s[i]*p[i]
print(result)