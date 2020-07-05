n = int(input())
articles = []
for i in range(n):
    articles.append([j for j in input().split()[1:]])
m = int(input())
for i in range(m):
    flag = False
    word = input()
    for j in range(n):
        if articles[j].__contains__(word):
            print(j+1, end=' ')
            flag = True
    if not flag:
        print(' ')
    else:
        print()