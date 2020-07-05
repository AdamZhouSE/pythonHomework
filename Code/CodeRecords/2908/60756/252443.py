N=int(input())
wordDicts=[]
def noEmpty(s:str):
    return s and s.strip()
for i in range(N):
    s=list(filter(noEmpty,list(input())))
    s.sort()
    wordDicts.append(''.join(s))
print(len(set(wordDicts)),end="")