l, m = list(map(int, input().split()))
s = input()
result = []
for i in range(m):
    a,b,c,d = list(map(int, input().split()))
    s1,s2 = s[a-1:b], s[c-1:d]
    if len(s2) < len(s1):
        s1, s2 = s2, s1
    while len(s1) > 0:
        if s2.startswith(s1):
            result.append(len(s1))
            break
        else:
            s1 = s1[:-1]

for i in result:
    print(i)