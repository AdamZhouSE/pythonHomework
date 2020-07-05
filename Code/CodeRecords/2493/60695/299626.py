n = int(input())
a = input().split(" ")
a = list(map(int, a))
m = int(input())
for i in range(m):
    r = input().split(" ")
    suba = []
    for j in range(int(r[0])-1, int(r[1])):
        suba.append(a[j])
    from collections import Counter
    c = Counter(suba)
    print(len(c))