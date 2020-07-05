
num=int(input())
test=input().split()

c1=0
ans=1
for x in test:
    if x=='1':
        c1+=1
c0=num-c1
count=[]
i=0
temp=str(''.join(test))

nt=temp.split('1')
nt.pop()
nt.pop(0)
for x in nt:
    count.append(len(x))
if c1==0:
    ans=0
elif c1==1:
    ans=1
else:
    for x in count:
        ans*=(x+1)
print(ans)