s = input()
suffix = dict()


for i in range(len(s)):
     suffix[s[i:]] = i + 1

words = list(suffix.keys())


for index in range(len(words) - 1):
    for j in range(index + 1, len(words)):
        if words[index][0] == words[j][0]:
            if len(words[index]) > len(words[j]):
                temp = words[j]
                words[j] = words[index]
                words[index] = temp
        else:
            if ord(words[index][0]) > ord(words[j][0]):
                temp = words[j]
                words[j] = words[index]
                words[index] = temp

for key in words:
    print(suffix[key], end=' ')