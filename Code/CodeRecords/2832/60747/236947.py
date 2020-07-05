n=int(input())
num = input().split(" ")
count = 0
for i in range(n):
    num[i]=int(num[i])
    if num[i]==i+1:
        count = count + 1
print(count)