# 判断 words2 是否可以接在 word1 的后面
def judge(word1, word2):
    if len(word2) != len(word1) + 1:
        return False
    dic1 = {}
    dic2 = {}
    for char in word1:
        dic1.setdefault(char, 0)
        dic1[char] += 1
    for char in word2:
        dic2.setdefault(char, 0)
        dic2[char] += 1
    key1 = list(dic1.keys())
    key2 = list(dic2.keys())
    for k in key1:
        if k not in key2:
            return False
        if dic1[k] > dic2[k]:
            return False
    return True


if __name__ == '__main__':
    words = []
    while True:
        try:
            words.append(input())
        except EOFError:
            break
    words.sort(key=lambda k: len(k))
    pair = []
    for i in range(0, len(words)):
        for j in range(0, len(words)):
            if judge(words[i], words[j]):
                pair.append([words[i], words[j]])
    temp = pair
    k = 0
    while k < 10:
        new_pair = []
        for i in range(0, len(temp)):
            for j in range(0, len(pair)):
                if temp[i][-1] == pair[j][0]:
                    t = temp[i].copy()
                    t.append(pair[j][1])
                    new_pair.append(t)
        try:
            if len(temp[0]) < len(new_pair[0]):
                temp = new_pair
        except IndexError:
            pass
        k += 1
    try:
        print(len(temp[0]))
        for i in temp[0]:
            print(i)
    except IndexError:
        print(1)
        print(words[0])
