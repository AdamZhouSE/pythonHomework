n = int(input())

count = 0
time = 0
for i in sorted(map(int, input().split())):
    if time <= i:
        time += i
        count += 1

print(count)
