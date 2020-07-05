n,d=map(int,input().split(' '))
arr=list(map(int,input().split(' ')))
sum=0
for i in range(n):
    for j in range(n):
        if(j!=i and abs(arr[j]-arr[i])<=d):
            sum+=1
print(sum)

