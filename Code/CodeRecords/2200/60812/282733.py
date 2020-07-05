s = input()
t = input()
k = int(input())
d = set()
sum, n = 0, len(s)
for i in range(n):
    for j in range(i+1, n+1):
        if t.count('0', i, j) <= k:
            temp = s[i:j]
            if temp not in d:
                sum += 1
                d.add(temp)
print(sum)