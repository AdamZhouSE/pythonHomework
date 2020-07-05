n=int(input())
power=0
num=list(input().split(" "))
for i in range(n):
    num[i]=int(num[i])
num.sort(reverse=True)
print(num[0])