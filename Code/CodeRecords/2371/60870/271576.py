num_test = int(input())
word_list = []
for i in range(num_test):
    word = input()
    words = []
    for ch in word:
        if 'Z' >= ch >= 'A' or 'z' >= ch >= 'a':
            words.append(ch)
    word = ''.join(words)
    word = word.lower()
    word_list.append(word)
for i in range(num_test):
    word = word_list[i]
    word_reverse = word[::-1]
    if word == word_reverse:
        print('YES')
    else:
        print('NO')