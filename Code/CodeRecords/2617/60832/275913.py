All = int(input())

for q in range(0, All):
    temp = input().split()
    binary = temp[0]
    k = int(temp[1])
    ans = 0
    length = len(binary)

    for i in range(length):
        for j in range(i + 1, length + 1):
            if binary[i:j].count('1') == k:
                ans += 1
    print(ans)
