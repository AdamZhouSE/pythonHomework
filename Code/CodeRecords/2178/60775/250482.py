
n = int(input())
num = input().split(' ')
all = []

for i in range(n):
    for j in range(i+1):
        if num[i-j:i+1] not in all:
            all.append(num[i-j:i+1])
    print(len(all))
