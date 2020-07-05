num_test = int(input())
text_list = []
word_list = []
for i in range(num_test):
    text = input()
    word = input()
    text_list.append(text)
    word_list.append(word)
for i in range(num_test):
    dict_goal = {}
    word = word_list[i]
    text = text_list[i]
    count = 0
    for ch in word:
        if ch in dict_goal.keys():
            dict_goal[ch] = dict_goal[ch] + 1
        else:
            dict_goal[ch] = 1
    for j in range(0, len(text) - len(word) + 1):
        dict_get = {}
        for k in range(j, j + len(word)):
            if text[k] in dict_get.keys():
                dict_get[text[k]] = dict_get[text[k]] + 1
            else:
                dict_get[text[k]] = 1
        if dict_get == dict_goal:
            count = count + 1
    print(count)