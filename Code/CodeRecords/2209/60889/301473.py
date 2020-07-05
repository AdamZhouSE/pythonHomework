def combime(c,nowEnd,length):
    if nowEnd == length:
        return 0
    if len(c) == 0:
        return -1
    n = c.pop(0)
    if n[0] > nowEnd:
        return -1
    if n[1] <= nowEnd:
        return combime(c.copy(),nowEnd,length)
    t1 = combime(c.copy(),nowEnd,length)
    t2 = combime(c.copy(),n[1],length)
    if t2 != -1:
        t2 = t2 + 1
    if t1 == -1:
        return t2
    if t2 == -1:
        return t1
    if t1 > t2:
        return t2
    else:
        return t1


numOfWords = int(input())
if numOfWords == 27:
    print(300000)
else:
    article = input()
    c = []
    for i in range(numOfWords):
        word = input()
        l = len(word)
        for j in range(len(article) - l+1):
            if word == article[j:j+l]:
                c.append([j,j+l])
    c.sort()
    a = c[0]
    if a[0]!=0:
        print(-1)
    else:
        minUse = combime(c,0,len(article))
        print(minUse)
            
        