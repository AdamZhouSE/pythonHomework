# leetcode 472 连接词

if __name__ == '__main__':
    words = input()[1:-1].split(",")
    for i in range(0, len(words)):
        words[i] = words[i][1:-1]
    sorted_words = sorted(words, key=lambda k: len(k))
    s = set(sorted_words)
    ans = []
    while sorted_words:
        word = sorted_words.pop(-1)
        s.remove(word)
        L = len(word)
        stack = [0]
        while stack:
            p = stack.pop(0)
            flag = False
            for i in range(p+1, L+1):
                if word[p:i] in s:
                    stack.append(i)
                    if i == L:
                        ans.append(word)
                        flag = True
                        break
            if flag:
                break
    # 这里已经求出了ans，但是是按长度排序的，要求按在原数组中的输入顺序排序
    index = []
    for item in ans:
        index.append(words.index(item))
    index.sort()
    ans = []
    for i in index:
        ans.append(words[i])
    print(ans)

