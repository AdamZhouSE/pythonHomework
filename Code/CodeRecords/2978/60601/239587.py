word = input().split(' ')
for i in range(word.count('')):
    word.remove('')
if word[0] == word[1]:
    print(0)
else:
    print(ord(word[0][0]) - ord(word[1][0]))