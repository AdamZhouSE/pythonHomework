t=int(input())
l=eval('['+input().replace(' ',',')+']')
cond=0
result='YES'
for i in range(len(l)-1):
    if cond==0:
        if l[i]>l[i+1]:
            result='NO'
        if l[i]==l[i+1]:
            cond=1
    if cond==1:
        if l[i]<l[i+1]:
            result='NO'
        if l[i]>l[i+1]:
            cond=2
    if cond==2:
        if l[i]<l[i+1]:
            result='NO'
print(result)