arr=list(map(int,input().split()))
n=arr[0]
l=arr[1]
r=arr[2]
min=0;
for i in range(l):
    min+=pow(2,i)
min+=n-l
max=0
for i in range(r):
    max+=pow(2,i)
max+=(n-r)*pow(2,r)
print(min,end=" ")
print(max)