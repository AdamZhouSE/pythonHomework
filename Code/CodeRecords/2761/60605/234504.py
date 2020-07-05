t = int(input())
li = []
for i in range(t):
    li.append(int(input()))

for i in range(t):
    sum = 0
    for j in range(1, li[i] + 1):
        sum += j*j
    print(sum)