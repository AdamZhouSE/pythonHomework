ar = list(map(int, input().split(',')))

if len(ar) == 1 or ar[0] > ar[1]:
    print(0)
    exit()

for i in range(1, len(ar) - 1):
    if ar[i] > ar[i + 1] and ar[i] > ar[i - 1]:
        print(i)
        exit()
print(len(ar) - 1)