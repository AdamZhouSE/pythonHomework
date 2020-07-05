N=int(input())
words=[]
for i in range(N):
    word=input()
    w=[]
    result=""
    for j in range(len(word)):
        w.append(word[j])
    w.sort()
    for j in range(len(word)):
        result+=w[j]
    words.append(result)
words=list(set(words))
print(len(words))