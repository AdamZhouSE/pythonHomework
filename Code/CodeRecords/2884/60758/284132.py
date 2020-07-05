n,k=int(input())
b=list(map(int,input().split()))
count=0
for i in range(0,n):
    for j in range(i+1,n):
        if(abs(b[i]-b[j])<=k):
            count+=2
print(count)