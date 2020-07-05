n=int(input())
a=list(map(int,input().split()))
sum=0
odda=[]
for i in range(n):
    k=a[i]
    if not k%2==0:
        odda.append(k)
    sum+=k
odda.sort(reverse=True)
sum=sum-odda[-1] if len(odda)%2==1 else sum
print(sum)
