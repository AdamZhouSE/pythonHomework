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
    for i in range(0, len(words)-1):
        for j in range(i+1, len(words)):
            if judge(words[i], words[j]):
                pair.append([words[i], words[j]])
    print(pair)

