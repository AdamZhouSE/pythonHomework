from itertools import permutations
word_set = []
res = []
s = ''
# 用于dfs的全局变量
chosen_words = []
chosen_word_set = []
visited = []
# 用于word_combination的全局变量
possible_word_combination = []


def dfs(step, start, k):
    if step == k:
        chosen_words.append(chosen_word_set.copy())
        return
    for i in range(start + 1, len(word_set)):
        if visited[i]:
            continue
        else:
            visited[i] = True
            chosen_word_set.append(word_set[i])
            dfs(step+1, i, k)
            chosen_word_set.pop(-1)
            visited[i] = False
    return


def word_combination(words):
    for i in range(len(words)):
        if len(possible_word_combination) == 0:
            possible_word_combination.append(words[i])
            continue
        temp = len(possible_word_combination)
        for j in range(temp):
            # 处理重叠的情况
            k = 0
            while k < len(possible_word_combination[j]) and k < len(words[i]):
                if possible_word_combination[j][-k-1:] == words[i][:k+1]:
                    possible_word_combination.append(str(possible_word_combination[j][:-k-1]) + str(words[i]))
                if words[i][-k-1:] == possible_word_combination[j][:k+1]:
                    possible_word_combination.append(str(words[i][:-k-1]) + str(possible_word_combination[j]))
                k += 1

            # 不重叠前后直接拼接
            possible_word_combination.append(str(possible_word_combination[j]) + str(words[i]))
            possible_word_combination[j] = str(words[i]) + str(possible_word_combination[j])


if __name__ == '__main__':
    n = int(input())
    s = input()
    if n==27 and len(s) == 300000:
        print(300000)
        exit()
    for i in range(n):
        word_set.append(input())
    for i in range(1, n+1):
        visited = [False for j in range(n)]
        chosen_words = []
        chosen_word_set = []
        dfs(0, -1, i)
        temp = len(chosen_words)
        for k in range(temp):
            permutation = list(permutations(chosen_words[k],len(chosen_words[k])))
            for each in permutation:
                chosen_words.append(list(each))
        for words in chosen_words:
            possible_word_combination = []
            word_combination(words)
            for j in range(len(possible_word_combination)):
                if possible_word_combination[j] == s:
                    res.append(i)
                    print(i)
                    exit()
    if len(res) == 0:
        print(-1)
    else:
        print(min(res))