n = int(input())
article = [0]
for i in range(n):
    inp = input().split(" ")
    command, data = inp[0], inp[1]
    if command == 'T':
        article.append(data)
    elif command == 'U':
        index = int(data)
        article = article[0: len(article)-index]
    else:
        index = int(data)
        print(article[index])
