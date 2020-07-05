
num=int(input())
book=[]
for n in range(num):
    word=input().split()
    
    word=list(''.join(word))
    word.sort()
    word=''.join(word)
    has=False

    for w in book:
        if w==word:
            has=True
    if not has:
        book.append(word)
print(len(book),end='')
    
    

