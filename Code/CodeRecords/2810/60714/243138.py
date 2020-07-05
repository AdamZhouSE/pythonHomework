temp = input()
n = []
for i in range(0, len(temp)):
    n.append(int(temp[i]))
print(max(n))
ans = []
for i in range(0, max(n)):
    temp = 0
    j = 0
    while j < len(n):
        while j < len(n) and n[j] is 0:
            j += 1
        if j < len(n) and n[j] is not 0:
            n[j] -= 1
            temp += pow(10, len(n) - j - 1)
        j += 1
    ans.append(temp)
for i in range(0, len(ans) - 1):
    print(ans[i], end=" ")
print(ans[len(ans) - 1])
