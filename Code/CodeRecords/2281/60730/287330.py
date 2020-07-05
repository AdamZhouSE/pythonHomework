num = int(input())
for i in range(num):
    m = int(input())
    n = list(map(int, input().split(" ")))
    ans, tmp = [], []
    for j in range(len(n)):
        if j == len(n) - 1:
            ans.append(n[j])
            break
        tmp = n[j + 1:]
        if n[j] >= max(tmp):
            ans.append(n[j])
    print(' '.join(list(map(str, ans))))
