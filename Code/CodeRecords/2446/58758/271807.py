N = int(input())
articles = []
for i in range(N):
    text = input().split()
    articles.append(text[1:])
M = int(input())
ans = []
for i in range(M):
    words = input()
    res = []
    for j in range(0, len(articles)):
        try:
            ind = articles[j].index(words)
            res.append(j+1)
        except Exception:
            pass
    ans.append(res)
for i in ans:
    if len(i) == 0:
        print(' ')
    else:
        for j in i:
            print(j, end=' ')
        print()
