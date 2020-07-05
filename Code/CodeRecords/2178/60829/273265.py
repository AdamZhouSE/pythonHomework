n = int(input())
ns = input().split(' ')
s = []
for i in range(n):
    for j in range(0, i+1):
        t = ns[j:i+1]
        if t not in s:
            s.append(t)
    print(len(s))