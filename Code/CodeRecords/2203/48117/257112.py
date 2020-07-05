s = input()

for i in range(len(s) - 1):
    count = 0
    for j in range(i + 1, len(s)):
        for l in range(len(s) - j):
            if s[i:i+l] == s[j:j+l]:
                count += l - 1

    print(count % (pow(10, 9) + 7))