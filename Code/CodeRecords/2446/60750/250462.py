def solve():
    n = int(input())
    article = []
    for i in range(0,n):
        data = input().split(' ')
        article.append(data[1:])

    m = int(input())
    res = []
    for i in range(0,m):
        word = input()
        tmp = []
        for j in range(0,n):
            for k in range(0,len(article[j])):
                if word == article[j][k]:
                    tmp.append(j + 1)
                    break
        res.append(tmp)
        
    for i in range(0,len(res)):
        if res[i] == []:
            print(' ')
           
            
        else:
            for j in range(0,len(res[i])):
                print(res[i][j],end = ' ')
            print()


solve()