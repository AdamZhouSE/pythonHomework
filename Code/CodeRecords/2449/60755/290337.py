num = input().split(",")
n = int(input())
for i in range(len(num)):
    num[i] = int(num[i])
res = -1
for i in range(len(num)):
    if num[i]==n:
        res = i
        break
print(res)