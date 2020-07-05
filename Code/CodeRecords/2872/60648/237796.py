n=input()
n=int(n)
s=input()
ls=[]
count=0
for i in range(n):
    ls.append(s[i])
print(ls)
t=0
while 1>0:
    if n=1:
        break
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
