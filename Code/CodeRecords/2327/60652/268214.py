s=input()
n=len(s)
upper=n
lower=0
a=[]
for i in range(n):
    if s[i]=='I':
        a.append(lower)
        lower+=1
    if s[i]=='D':
        a.append(upper)
        upper-=1
if s[n-1]=='I':
    a.append(lower)
    lower+=1
if s[n-1]=='D':
    a.append(upper)
    upper-=1      
print(a) 