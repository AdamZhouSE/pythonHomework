n=input()
n=int(n)
ls=input().split(" ")
#print(ls)
#ls=[int(ls[i]) for i in range(n)]
count=0
count1=0
for x in ls:
    if x=='0':
        count=count+1
if count==0:
    print(-1)
for x in ls:
    if x=='5':
        count1=count1+1
if count1%9==0:
    print(int('5'*count1+'0'*count))
else:
    print(0)