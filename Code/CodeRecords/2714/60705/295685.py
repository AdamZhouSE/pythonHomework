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
    print(words)
    ans = []
    for i in range(0, len(words)):
        temp_ans = [words[i]]
        j = i+1
        while j < len(words):
            if judge(temp_ans[-1], words[j]):
                temp_ans.append(words[j])
                if len(temp_ans) > len(ans):
                    ans = temp_ans
            j += 1
    print(len(ans))
    for a in ans:
        print(a)

