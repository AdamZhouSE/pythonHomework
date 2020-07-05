v=int(input())
nd=list(map(int,input().split()))
S=[0]*11
lst=10**5
nb=0
for i in range(1,10):
    S[i]=nd[i-1]
    if(lst>=nd[i-1]):
        lst=nd[i-1]
        nb=i
if(v<lst):
    print(-1)
else:
    ans=[]
    t=v//lst
    for i in range(t,0,-1):
        for j in range(9,0,-1):
            if(S[j]>v):
                continue
            if(v-S[j]<(i-1)*lst):
                continue
            ans.append(str(j))
            v-=S[j]
            break
    print(''.join(ans))