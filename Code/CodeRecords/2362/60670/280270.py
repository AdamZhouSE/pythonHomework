n=int(input())
group=(n+3)//4
answer=0
for i in range(0,group):
    t=n-i*4
    tmp=t
    if t-1>0:
        tmp*=(t-1)
    if t-2>0:
        tmp=tmp//(t-2)
    if i==0:
        if t-3>0:
            tmp+=(t-3)
        answer=tmp
    else:
        if t-3>0:
            tmp-=(t-3)
        answer-=tmp
print(answer)