n = int(input())
s = input().split()
sum = 0
max = 0
for x in s:
    if int(x) > max:
        max = int(x)
    sum += int(x)
print(max * n - sum)
