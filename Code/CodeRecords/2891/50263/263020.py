n = int(input())
list = input().split()
count = 0
for i in range(n):
    list[i] = int(list[i])
for i in range(n):
    count = count + max(list) - list[i]
print(count)