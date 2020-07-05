n = int(input())
s = set()
l = len(s)
for i in range(n):
    s.add(input())
    print("YES" if len(s)==l else "NO")
    l = len(s)
    