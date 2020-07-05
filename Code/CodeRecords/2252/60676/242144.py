def find_words(text, word):
    count = 0
    new_word = destructor(word)
    for i in range(len(text)-len(word)+1):
        if destructor(text[i:i+len(word)]) == new_word:
            count += 1
    return count


def destructor(word):
    elements = []
    for i in range(len(word)):
        elements.append(word[i])
    elements.sort()
    std_word = ''
    for i in range(len(elements)):
        std_word += elements[i]
    return std_word


result = []
for i in range(int(input())):
    result.append(find_words(input(), input()))
for i in range(len(result)):
    print(result[i])