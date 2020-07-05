num=int(input())
arr=input().split()
for i in range(0,num):
    arr[i]=int(arr[i])
sum=0
for i in range(0,num):
    sum=sum+arr[i]
max=sum
for i in range(0,num):
    B=0
    C=0
    for m in range(0,i):
        B=B+arr[m]
    C=sum-B
    if B-C>max:
        max=B-C
print(max)
