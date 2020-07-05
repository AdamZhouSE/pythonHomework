def insert(trietree: list, word):
    for i in trietree:
        if i[0][0] == word[0]:
            if len(word) == 1:
                i[0][1] += 1
            else:
                insert(i[1], word[1:])
            break
    else:
        tree = trietree
        n = len(word)
        for i in range(n):
            num = 0
            if i == n-1:
                num = 1
            temp = []
            tree.append([[word[i], num], temp])
            tree = temp


def delete(trietree, word):
    for i in trietree:
        if i[0][0] == word[0]:
            if len(word) == 1:
                i[0][1] -= 1
            else:
                delete(i[1], word[1:])


def search(trietree, word):
    label = False
    for i in trietree:
        if i[0][0] == word[0]:
            if len(word) == 1:
                if i[0][1] != 0:
                    label = True
            else:
                label = search(i[1], word[1:])
            break
    return label


def count(trietree, word):
    num = 0
    for i in trietree:
        if i[0][0] == word[0]:
            if len(word) == 1:
                num += i[0][1]
                s = [i[1]]
                while s:
                    temp = s.pop()
                    for j in temp:
                        num += j[0][1]
                        if j[1]:
                            s.insert(0, j[1])
            else:
                num += count(i[1], word[1:])
            break
    return num

m = int(input())
trietree = []
for i in range(m):
    op, word = input().split()
    if op == '1':
        insert(trietree, word)
    elif op == '2':
        delete(trietree, word)
    elif op == '3':
        if search(trietree, word):
            print('YES')
        else:
            print('NO')
    else:
        print(count(trietree, word))