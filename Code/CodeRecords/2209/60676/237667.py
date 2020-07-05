import math

# word类，拥有内容和权值两个属性
class Word:
    def __init__(self, content, key):
        self.content = content
        self.key = key


# 根据所给长度大于一的单词的公共部分判断是否能拼接成更大的单词
def compound_words(word_list):
    new_list = []
    for i in range(len(word_list)):
        if len(word_list[i].content) > 1:
            new_list.append(word_list[i])
    ex_list = word_list.copy()
    if len(new_list) > 1:
        for i in range(len(new_list) - 1):
            for j in range(i + 1, len(new_list)):
                compound = compound_word(new_list[i], new_list[j])
                if len(compound) > 0:
                    for k in range(len(compound)):
                        exist = False
                        for l in range(len(word_list)):
                            if word_list[l].content == compound[k].content:
                                exist = True
                        if not exist:
                            ex_list.insert(0, compound[k])
    return ex_list


def compound_word(str1, str2):
    if len(str1.content) <= len(str2.content):
        for i in range(len(str2.content) - len(str1.content) + 1):
            if str2.content[i:i + len(str1.content)] == str1.content:
                return []
    else:
        for i in range(len(str1.content) - len(str2.content) + 1):
            if str1.content[i:i + len(str2.content)] == str2.content:
                return []
    new_list = []
    for i in range(1, min(len(str1.content), len(str2.content))+1):
        if str1.content[:i] == str2.content[-i:]:
            new_list.append(Word(str2.content + str1.content[i:], str1.key + str2.key))
        if str1.content[-i:] == str2.content[:i]:
            new_list.append(Word(str1.content + str2.content[i:], str1.key + str2.key))
    return new_list


num = int(input())
article = input()
real_list = []
for i in range(num):
    word = Word(input(), 1)
    if len(real_list) == 0:
        real_list.append(word)
    elif len(word.content) <= len(real_list[-1].content):
        real_list.append(word)
    else:
        index = 0
        while len(word.content) < len(real_list[index].content):
            index += 1
        real_list.insert(index, word)
extra_list = compound_words(real_list)
extra_list = compound_words(extra_list)
sum = 0

while len(extra_list) > 0:
    if len(extra_list[0].content) == 1:
        sum += len(article)
        break
    index = article.find(extra_list[0].content)
    while index != -1:
        article = article[:index] + article[index + len(extra_list[0].content):]
        sum += extra_list[0].key
        index = article.find(extra_list[0].content)
    extra_list.remove(extra_list[0])

print(sum)
