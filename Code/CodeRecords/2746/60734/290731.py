def one_letter_different(x,y):
    cnt = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            cnt += 1
        if cnt > 1:
            return False
    return cnt == 1

def find_next_word(words, beginword, endword, route):
    if beginword == endword:
        transform_list.append(route.copy())
        return

    for i in range(len(words)):
        if one_letter_different(words[i], beginword):
            route.append(words[i])
            next_words = words[:i]+words[i+1:]
            find_next_word(next_words, words[i], endword, route)
            route.pop()


import re
beginword = input()
endword = input()
words = re.findall(r'"(.*?)"', input())

transform_list = []
find_next_word(words,beginword,endword,[beginword])
if transform_list:
    print(len(min(transform_list, key=len)))
else:
    print(0)