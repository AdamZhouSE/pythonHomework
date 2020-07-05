n = int(input())
for i in range(0, n):
    s = input()
    maxi = -1
    for i in range(0, len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j] and j - i - 1 > maxi:
                maxi = j - i - 1
    print(maxi)

