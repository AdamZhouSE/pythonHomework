def classify_words(words):
    classified_words = []
    for i in range(len(words)):
        a = standardize(words[i])
        if a not in classified_words:
            classified_words.append(a)
    return len(classified_words)


def standardize(word):
    elements = []
    for i in range(len(word)):
        if word[i] != ' ':
            elements.append(word[i])
    elements.sort()
    std_word = ''
    for i in range(len(elements)):
        std_word += elements[i]
    return std_word


array = []
for i in range(int(input())):
    array.append(input())
print(classify_words(array), end='')