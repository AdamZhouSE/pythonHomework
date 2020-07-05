a=int(input())
b=input().split(' ')
b=list(map(int,b))
res=0
for i in range(1,a-1):
    if b[i]==0 and b[i+1]==1 and b[i-1]==1:
        b[i+1]=0
        res+=1

print(abs(res))