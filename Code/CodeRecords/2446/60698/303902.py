def test():
    n = int(input())
    articles = []
    for _ in range(0, n):
        article = input().split()
        article = article[1:]
        articles.append(article)
    m = int(input())
    for _ in range(0, m):
        word = input()
        res = []
        for i in range(0, len(articles)):
            if word in articles[i]:
                res.append(i + 1)
        if res:
            print(0)
        else:
            print(' '.join(list(map(str, res))))

test()