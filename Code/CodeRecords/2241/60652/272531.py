n=int(input())
count=0
if n==1:
    count=1
for i in range(1,n+1):
    if n%i==0 and i!=n+1 and i%2!=0:
        count+=1
print(count)        