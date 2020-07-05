t = int(input())

for c in range(t):
    num = int(input())
    count = 0
    for i in range(num // 10 + 1):
        for j in range((num - i * 10) // 5 + 1):
            if (num - i * 10 - j * 5) % 3 == 0:
                count += 1
    print(count)
