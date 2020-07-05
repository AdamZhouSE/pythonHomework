def sum():
    l=list(map(int,input().split(" ")))
    sum=0
    for i in l:
        sum+=i
    return sum


n=int(input())
dict={}
for i in range(0,n):
    dict[i+1]=sum()
rank=n+1    
for j in range(1,n+1):
    if dict[j]<=dict[1]:
        rank-=1
print(rank)        