def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


data = list(map(int, input().split(',')))
c = 0
for i in range(len(data) - 2):
    for j in range(i + 1, len(data) - 1):
        for k in range(j + 1, len(data)):
            c = data[i] + data[j] + data[k] if is_triangle(data[i], data[j], data[k]) and data[i] + data[j] + data[k] > c else c
print(c)
