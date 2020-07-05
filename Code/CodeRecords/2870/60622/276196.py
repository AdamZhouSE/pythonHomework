n=int(input())
l=list(map(int,input().split()))
count=0
odd=[]
for i in range(n):
    if l[i]%2==0:
        count+=l[i]
    else:
        odd.append(l[i])
odd.sort()
sum=0
for e in odd:
    sum+=e
if len(odd)%2!=0:
    sum=sum-odd[0]
print(sum+count)