n=int(input())
m=int(input())
p=int(input())
times=p/m
i=1
while(pow(i,times)<=n/2):
    i=i+1
print(i)