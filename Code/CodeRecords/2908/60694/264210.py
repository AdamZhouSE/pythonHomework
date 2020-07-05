N = int(input())
words = [input().strip() for _ in range(N)]
a_set = set()
for word in words:
    l = list(word)
    l.sort()
    s = ''.join(l)
    a_set.add(s)
ans = len(a_set)
print(ans, end="")
