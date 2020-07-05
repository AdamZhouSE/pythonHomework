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
else:
    for j in ls:
        if j=='5':
            count1=count1+1
    if count1%9==0:
        if count==n:
            print(0)
        else:
            print(int('5'*count1+'0'*count))
    else:
        print(0)