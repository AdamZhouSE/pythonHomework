n = int(input())
list = input().split()
count = 0
for i in range(n):
    list[i] = int(list[i])
for i in range(1,n-1):
    if (list[i] < list[i-1] and list[i] < list[i+1]) or (list[i] > list[i-1] and list[i] > list[i+1]):
        count = count + 1
print(count)