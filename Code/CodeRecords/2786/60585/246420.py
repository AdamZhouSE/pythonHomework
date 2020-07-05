n=eval(input())
num=input().strip().split(' ')
num=[int(i) for i in num]
num=sorted(num)
k=1
for i in range(n):
    if num[i]>=k:k+=1
print(k-1)