num = int(input())
for i in range(num):
    m = int(input())
    n = [1, 1, 1]
    if m < len(n):
        print(n[m])
        continue
    for j in range(3, m + 1):
        n.append(n[j - 2] + n[j - 3])
    print(n[m])
