n=input().split(' ')
N=int(n[0])
Q=int(n[1])
li1=[]
li2=[]
for i in range(N):
    li1.append(0)
    li2.append(0)
for i in range(Q):
    s=input().split(' ')
    I=s[0]
    zhan=int(s[1])
    chil=int(s[2])
    if(s[0]=='M' and li2[chil-1]==0):
        li2[chil-1]=chil
        li1[chil-1]=zhan
        continue
    if(s[0]=='D'):
        num=0
        for k in range(chil-1,len(li2)):
            if(li2[k]!=0):
                if(li1[k]<=zhan):
                    print(li2[k])
                    num=1
                    break
        if(num==0):
            print(-1)
        continue