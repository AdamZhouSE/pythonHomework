s = input()
suffix = dict()


for i in range(len(s)):
     suffix[s[i:]] = i + 1

words = list(suffix.keys())


words.sort()

for l in range(len(words)):
    if l != len(words) - 1:
        print(suffix[words[l]], end=' ')
    else:
        print(suffix[words[l]])