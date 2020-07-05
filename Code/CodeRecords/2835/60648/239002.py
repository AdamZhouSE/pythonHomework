n=input()
n=int(n)
ls=input().split(" ")
#print(ls)
#ls=[int(ls[i]) for i in range(n)]
count=0
for x in ls:
    if x=='0':
        count=count+1
if count==0:
    print(-1)