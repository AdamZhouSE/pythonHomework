num=int(input())
for i in range(num):
    text=input()
    word=list(input())
    word.sort()
    word=''.join(word)
    count=0
    for a in range(len(text)-len(word)+1):
        cut=list(text[a:a+len(word)])
        cut.sort()
        cut=''.join(cut)
        if word==cut:
            count+=1
    print(count)
        
        

