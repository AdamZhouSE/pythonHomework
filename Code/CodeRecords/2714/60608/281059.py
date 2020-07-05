

def cat(words: list, word: str, path: list, res: list):
    for item in words:
        end = True
        if len(item) - len(word) == 1:
            s, flag = set(list(word)), True
            for char in s:
                if word.count(char) > item.count(char):
                    flag = False
                    break
            if flag:
                end = False
                res.append(item)
                cat(words, item, path, res)
                del res[-1]
    if end and len(path[0]) < len(res):
        path[0] = res[:]


def func13():
    words = []
    while True:
        try:
            t = input()
            if t:
                words.append(t)
            else:
                break
        except:
            break
    words = sorted(words, key=lambda x: len(x))
    path, res = [[]], []
    for word in words:
        res.append(word)
        cat(words, word, path, res)
        del res[-1]

    print(len(path[0]))
    for word in path[0]:
        print(word)


func13()
