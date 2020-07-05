inp = input().split(" ")
n=int(inp[0])
t=int(inp[1])
c=int(inp[2])
harm=input().split(" ")
for i in range(n):
    harm[i]=int(harm[i])
isornot=[]
res=0
zeronum = 0
for i in range(n):
    isornot.append(0)
    if(harm[i]>t):isornot[i]='n'
for i in range(n):
    if(isornot[i]==0):
        zeronum+=1
        if(i==n-1):isornot[i]=zeronum
    else:
        isornot[i-1]=zeronum
        zeronum=0
for i in range(n):
    if(isornot[i]!=0 and isornot[i]!='n'):
        if(isornot[i]>=c):
            res = res+1+isornot[i]-c
            
print(res)
        