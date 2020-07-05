num=int(input())
words=[]
for i in range(num):
    word=list(input())
    word.sort()
    word=''.join(word)
    words.append(word)
words=set(words)
print(len(words))