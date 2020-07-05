s=eval(input())
t=[]
for i in s:
    tmp=list(i.split(':'))
    t.append(60*int(tmp[0])+int(tmp[1]))
t.sort()
minn=24*60-t[len(t)-1]+t[0]
for i in range(len(t)-1):
    minn=min(minn,t[i+1]-t[i])
print(minn)