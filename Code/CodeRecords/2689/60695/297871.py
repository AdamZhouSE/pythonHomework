from collections import Counter
t = int(input())
for i in range(t):
    ab = input().split(" ")
    s = ab[0]+ab[1]
    c = Counter(s)
    print(len(c))