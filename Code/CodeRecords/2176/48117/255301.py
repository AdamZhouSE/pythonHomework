s = input()
suffix = dict()


for i in range(len(s)):
     suffix[s[i:]] = i + 1

words = suffix.keys()
val = suffix.get()

for index in range(len(words) - 1):
    if words[index][0] == words[index + 1][0]:
        if len(words[index]) > len(words[index + 1]):
            temp = words[index + 1]
            words[index + 1] = words[index]
            words[index] = temp
    else:
        if ord(words[index][0]) > ord(words[index + 1][0]):
            temp = words[index + 1]
            words[index + 1] = words[index]
            words[index] = temp

for key in words:
    print(suffix[key], end=' ')