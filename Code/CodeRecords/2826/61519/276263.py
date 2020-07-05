n=int(input())
key=0
num=list(input().split(" "))
for i in range(n):
    num[i]=int(num[i])
num.sort()
for i in range(n-1):
    for j in range(i+1,n):
        if num[i]==num[j]:
            num[j]=num[j]+(j-i)
            key=key+(j-i)
print(key)