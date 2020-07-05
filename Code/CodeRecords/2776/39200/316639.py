words = input()[2:-2].split('","')
wordlist = sorted(words, key = lambda i:len(i))
s = set(wordlist)
res = []
while s:
    word = wordlist.pop(-1)
    s.remove(word)
    length = len(word)
    stack = [0]
    while stack:
        p = stack.pop(0)
        flag = 0
        for i in range(p + 1, length + 1):
            if word[p:i] in s:
                stack.append(i)
                if i == length:
                    res.append(word)
                    flag = 1
                    break
        if flag:
            break
newres = []
for x in wordlist:
    if x in res:
        newres.append(x)
print(newres)
