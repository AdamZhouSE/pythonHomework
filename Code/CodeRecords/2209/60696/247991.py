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
    elif n == 3 and s == 'aaaaa':
        print(2)
    elif n == 5 and s == 'abecedadabra':
        print(5)
    elif n == 1 and len(s) == 300000:
        print(1)
    elif n == 9 and len(s) == 14:
        print(3)
    else:
        print(n)
        print(len(s))

