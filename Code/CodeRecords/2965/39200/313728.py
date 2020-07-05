k, M = [int(x) for x in input().split()]
s = input()
N = int(input())
for i in range(N):
    Ai, Bi, Ci = [int(x) for x in input().split()]
    news = s[:Ci] + s[Ai:Bi] + s[Ci:]
    s = news[:M]
print(s[:k], end = "")
