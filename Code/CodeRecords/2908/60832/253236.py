num = int(input())

dic = {}
for i in range(0, num):
    word = list(input().strip(" "))

    word.sort()
    word = str(word)
    dic[word] = 1

print(len(dic),end='')
