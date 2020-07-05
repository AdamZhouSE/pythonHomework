a = [-99999999] + list(map(int, input().split(","))) + [99999999999999999]
for i in range(1, len(a) - 1):
    if a[i] > a[i - 1] and a[i] > a[i + 1]:
        print(i - 1)
        exit()
print(5)