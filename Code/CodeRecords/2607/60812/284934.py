T = int(input())
for i in range(T):
    s = input()
    n = len(s)
    count = 0
    for i in range(n-2):
        for j in range(i+3, n+1, 3):
            if s.count('0', i, j) == s.count('1', i, j) == s.count('2', i, j):
                count += 1
    print(count)