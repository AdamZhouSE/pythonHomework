n = int(input())
lst = sorted(list(map(int, input().split(' '))))
count = 0
time = 0
for i in lst:
    if i >= time:
        count += 1
        time += i
print(count)
