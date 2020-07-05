temp = input()
ans = 0
for i in range(0, len(temp)):
    if temp[i] is 'Q':
        foundA = 0
        for j in range(i + 1, len(temp)):
            if temp[j] is 'Q' and foundA is not 0:
                ans += foundA
            if temp[j] is 'A':
                foundA += 1
print(ans, end="")
