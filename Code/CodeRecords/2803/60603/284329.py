string=input().split(" ")
n=int(string[0])
m=int(string[1])
list=[]
for i in range(m):
    list.append(0)
for i in range(n):
    string=input().split(" ")
    for s in range(len(string)):
        list[int(string[s])-1]=1
sig=0
for i in range(m):
    if(list[i]!=1):
        sig=1
        break
if(sig==1):
    print("NO")
else:
    print("YES")