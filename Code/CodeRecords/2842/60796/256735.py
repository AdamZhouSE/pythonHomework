n=int(input())
ls=[]
r=[]#这个数组是每一个人不能与之在同一组的雇员的下标
for i in range(n):
    s=int(input())
    if s!=-1:
        s=s-1
    ls.append(s)

for i in range(n):
    string=""
    if ls[i]!=-1:
        leader=ls[i]
        while leader!=-1:
            string=string+" "+str(leader)
            leader=ls[leader]
    r.append(string)

max=0
for i in range(len(r)):
    n=r[i].count(" ")+1
    if n>max:
        max=n

print(max)