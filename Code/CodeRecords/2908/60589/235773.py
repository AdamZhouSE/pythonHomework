num=int(input())
words=[]
for i in range(num):
    word=list(input())
    word.sort()
    word=''.join(word).strip()
    words.append(word)
words=set(words)
print(len(words),end='')