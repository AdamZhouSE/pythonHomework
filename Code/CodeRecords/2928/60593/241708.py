v=int(input())
nd=list(map(int,input().split()))
S=[]
for i in range(1,10):
    S.append((i,nd[i-1]))
S.sort(key=lambda x:x[1])
t=v//S[0][1]-1
out=[str(S[0][0])]*(t)
v-=t*S[0][1]
for i in range(9,0,-1):
    if(v>=S[i][1]):
        print(''.join([str(i)].extend(out)))
        break