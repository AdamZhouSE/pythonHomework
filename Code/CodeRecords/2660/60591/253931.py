n = eval(input())
article = []
while(n != 0):
    n -= 1
    ops = input().split(" ")
    if(ops[0] == 'T'):
        article.append(ops[1])
    elif(ops[0] == 'U'):
        for x in range(eval(ops[1])):
            article.pop()
    elif(ops[0] == 'Q'):
        print(article[eval(ops[1]) - 1])