num=int(input())
list=input().split(" ")
for i in range(num):
    list[i]=int(list[i])
    list[i]-=1
sig=0
for i in range(num):
    stan=list[i]
    stan=list[stan]
    if(list[stan]==i):
        sig=1
        break
if(sig==1):
    print("YES")
else:
    print("NO")