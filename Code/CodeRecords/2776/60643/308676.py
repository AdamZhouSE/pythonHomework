from typing import List


def findAllConcatenatedWordsInADict(words: List[str]) -> List[str]:
    words = sorted(words, key=lambda i: len(i))
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
            for i in range(p + 1, L + 1):
                if word[p:i] in s:
                    stack.append(i)
                    if i == L:
                        ans.append(word)
                        flag = True
                        break
            if flag: break
    return ans

if __name__=="__main__":
    strs=eval(input())
    ans=findAllConcatenatedWordsInADict(strs)
    tmp=[]
    for i in strs:
        if i in ans:
            tmp.append(i)
    print(tmp)