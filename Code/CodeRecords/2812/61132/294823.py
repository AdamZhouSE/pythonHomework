n=int(input())
l=list(map(int,input().split()))
Max=max(l)
Min=min(l)
sum=0
for i in range(max(Min,1),Max+1):
    if l.count(i)!=0:
        sum+=1
print(sum)