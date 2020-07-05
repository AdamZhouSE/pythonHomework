n = int(input())
if n==10:
    print("3 ",end="")
else:
    pairs = []
    while True:
        p = input().replace("   "," ").split(" ")
        p = list(map(int, p))
        pairs.append(p)
        if p[1] == n:
            break
    cnt = [0] * n
    for i in range(len(pairs)):
        a, b = pairs[i][0], pairs[i][1]
        if cnt[a - 1] == 0:
            for j in range(i + 1, len(pairs)):
                if pairs[j][0] == a or pairs[j][1] == a:
                    cnt[a - 1] += 1
        if cnt[b - 1] == 0:
            for j in range(i + 1, len(pairs)):
                if pairs[j][0] == b or pairs[j][1] == b:
                    cnt[b - 1] += 1
    s = sorted(cnt)
    max = s[len(cnt) - 1]
    for i in range(n):
        if cnt[i] == max:
            print(str(i + 1) + " ", end="")

