subs = eval(input())
newsub = []
for sub in subs:
    for n in sub:
        newsub.append(n)
newsub.sort()
print(newsub)
