from typing import List


def findAllConcatenatedWordsInADict(words):
    words = sorted(words,key=lambda i:len(i))
    s = set(words)
    ans = []
    while words:
        word = words.pop(-1)
        s.remove(word)
        L = len(word)
        stack = [0]
        while stack:
            p = stack.pop(0)
            flag = False
            for i in range(p+1,L+1):
                if word[p:i] in s:
                    stack.append(i)
                    if i == L:
                        ans.append(word)
                        flag = True
                        break
            if flag:break
    ans.sort()
    return ans


aaa=input()
aaa=aaa[1:len(aaa)-1]
l=aaa.split(",")
inn=[]
for x in l:
    inn.append(x[1:len(x)-1])
print(findAllConcatenatedWordsInADict(inn))
        