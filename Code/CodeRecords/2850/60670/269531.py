n=int(input())
number=list(map(int,input().split()))
num_of_1=[0 for i in range(0,n+1)]
num_of_0=[0 for i in range(0,n+1)]
for i in range(1,n+1):
    num_of_0[i]=num_of_0[i-1]
    num_of_1[i]=num_of_1[i-1]
    if number[i-1]==1:
        num_of_1[i]+=1
    else:
        num_of_0[i]+=1
tot=num_of_1[n]
maxn=0
for i in range(1,n+1):
    for j in range(0,i):
        if num_of_0[i]-num_of_0[j]-num_of_1[i]+num_of_1[j]>maxn:
            maxn=num_of_0[i]-num_of_0[j]-num_of_1[i]+num_of_1[j]
print(maxn+tot)