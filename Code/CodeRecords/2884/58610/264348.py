num, diff = list(map(int, input().split(' ')))
height = sorted(list(map(int, input().split(' '))))
count = 0
for i in range(num):
    for j in range(num):
        if i != j and abs(height[i] - height[j]) <= diff:
            count += 1
print(count)