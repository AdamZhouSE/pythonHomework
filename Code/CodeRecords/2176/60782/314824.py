something = input()
dic = {}
word = []
for c in range(len(something)):
    dic.update({something[c:]:(c + 1)})
    word.append(something[c:])
word.sort()
for i in range(len(word) - 1):
    print(dic[word[i]],end=" ")
print(dic[word[len(word) - 1]])