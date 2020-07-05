def parts(words, word):
    if word in words:
        return True

    for i in range(len(words)):
        if words[i] in word:
            tmp = word.replace(words[i],'')
            words_temp = words[:i]+words[i+1:]
            if parts(words_temp, tmp):
                return True
    return False


import re
words = list(enumerate(re.findall(r'"(.*?)"', input())))
words = sorted(words, key=lambda x: len(x[1]))
valid = []
for i in range(1, len(words)):
    pure_words = [words[j][1] for j in range(i)]
    if parts(pure_words, words[i][1]):
        valid.append(words[i])
valid = sorted(valid, key=lambda x: x[0])
valid = [x[1] for x in valid]
print(valid)