nd=input().split(' ')
n=int(nd[0])
d=int(nd[1])
b=input().split(' ')
b=list(map(int,b))
count=0
for i in range(1,n):
    while b[i-1]>=b[i]:
        b[i]+=d
        count+=1
print(count)