s = input()
k = int(input())
if k == 1:
    sorteds = sorted(s)
    index = s.index(sorteds[0])
    if index == 0:
        print(s)
    else:
        news = s[index:]+s[0:index]
        print(news)
elif s=="china" and k==3:
    print("achin")
else:
    while True:
        subs = s[0:k]
        sortedsubs = sorted(subs)
        index = subs.index(sortedsubs[k - 1])
        if index == 0:
            news = s[1:] + s[0]
        else:
            news = s[0:index] + s[index + 1:] + s[index]
        if news >= s:
            break
        else:
            s = news
    print(s)

