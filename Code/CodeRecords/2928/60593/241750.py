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
t=v//lst-1
out=[str(nb)]*(t)
v-=t*lst
for i in range(9,0,-1):
    if(v>=S[i]):
        out.append(str(i))
        print(''.join(out))
        break