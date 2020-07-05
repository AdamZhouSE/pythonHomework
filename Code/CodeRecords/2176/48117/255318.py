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

for l in range(len(words)):
    if l != len(words) - 1:
        print(suffix[words[l]], end=' ')
    else:
        print(suffix[words[l]], end='')