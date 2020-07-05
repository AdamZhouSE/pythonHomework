a=int(input())
b=input().split(' ')
b=list(map(int,b))
lim=0
for i in range(1,a-1):
    if (b[i]<b[i-1] and b[i]<b[i+1]) or (b[i]>b[i-1] and b[i]>b[i+1]):
        lim+=1
print(lim)