s=input()
st=int(input())
num,bns,tmp,pos=[0]*1000,[0]*100,[0]*10000,0
for i in range(len(s)):
    num[i+1]=ord(s[i])-ord('A')+st
for i in range(1,len(s)+1):
    tot=0
    while(num[i]):
        tot+=1
        bns[tot]=num[i]%10
        num[i]//=10
    for i in range(tot,0,-1):
        pos+=1
        tmp[pos]=bns[i]
while(1):
    if(pos<=2):
        break
    if(pos==3 and tmp[1]==1 and tmp[2]==0 and tmp[3]==0):
        break
    for i in range(1,pos):
        num[i]=(tmp[i]+tmp[i+1])%10
    for i in range(1,pos):
        tmp[i]=num[i]
    pos-=1
flag=0
for i in range(1,pos+1):
    if(tmp[i]!=0):
        flag=1
        for j in range(i,pos+1):
            print(tmp[j],end='')
        break
if(not flag):
    print(0)