n=input()
n=int(n)
s=input()
ls=[]
count=0
for i in range(n):
    ls.append(s[i])
t=0
while t>=0:
    if ls[t]==ls[t+1]:
        ls.remove(ls[t])
        count=count+1
    else:
        t=t+1 
    if t==len(ls)-1:
        t=t+1
    if t+count+1==n:
        break
print(count)
        