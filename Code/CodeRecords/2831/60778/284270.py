rb=input()
distance=list(map(int,input().split()))
st=list(map(int,input().split()))
s=min(st)
t=max(st)
res_1=0
res_2=0
for i in range(len(distance)):
    if(i+1>=s and i+1<t):
        res_1+=distance[i]
    else:
        res_2+=distance[i]
if(res_1>res_2):
    print(res_2)
else:
    print(res_1)