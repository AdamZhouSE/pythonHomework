a=int(input())
b=1
i=1
m=1
t=1
g=[0,0,0,0,0,0,0,0,0,0]
while a>0:
    b=a%10
    i=9
    while i>9-b:
        g[i]=g[i]+t
        i=i-1
    if b>m:
        m=b
    t*=10
    a=int(a/10)
print(m)
ans=[]
for i in range(10):
		if g[i]!=0:
			ans.append(g[i])
for i in range(len(ans)):
    for j in range(i+1,len(ans)):
        if ans[i]<ans[j]:
            ans[i],ans[j]=ans[j],ans[i]
str1=''
for i in range(len(ans)-1):
    str1=str1+str(ans[i])+' '
str1=str1+str(ans[len(ans)-1])
print(str1)