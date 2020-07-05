def is_avail(word0, word1):
    if len(word0) != len(word1):
        return False

    diff_index = []
    i = 0
    while i < len(word0):
        if word0[i] != word1[i]:
            diff_index.append(i)
        if len(diff_index) > 2:
            return False
        i += 1

    if len(diff_index) != 2:
        return False

    if word0[diff_index[0]] == word1[diff_index[1]] and \
            word0[diff_index[1]] == word1[diff_index[0]]:
        return True

    return False


def func():
    words = input()[2:-2].split("\",\"")
    groups = [[words[0]]]
    words.pop(0)
    for word in words:
        i = 0
        flag = False
        break_flag = False
        while i < len(groups):
            j = 0
            while j < len(groups[i]):
                if is_avail(word, groups[i][j]):
                    groups[i].append(word)
                    break_flag = True
                    flag = True
                if break_flag:
                    break
                j += 1
            if break_flag:
                break
            i += 1
        if not flag:
            groups.append([word])

    # print(groups)
    print(len(groups))


func()
