N = int(input())
set1 = set()
s = ''
for tail in input().split():
    s = s + tail
    for i in range(len(s)):
        set1.add(s[i:])
    print(len(set1))