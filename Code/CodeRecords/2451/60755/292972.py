s = input().split(",")
n = int(input())
for i in range(len(s)):
    s[i] = int(s[i])
s.append(n)
s.sort()
for i in range(len(s)):
    if s[i]==n:
        print(i)
        break