arr=list(map(int,input().replace('[','').replace(']','').split(',')))
n=len(arr)
lower=int(input())
upper=int(input())
counter=0
for i in range(n):
    for j in range(i,n):
        s=sum(arr[i:j+1])
        if s>=lower and s<=upper:
            counter+=1
print(counter)        