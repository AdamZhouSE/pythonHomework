def count(s,text):
    n=len(s)
    N=len(text)
    result=0
    for i in range(N-n+1):
        currentArea=text[i:i+n]
        if sorted(currentArea)==sorted(s):
            result+=1
        else:
            continue
    print(result)


t=int(input())
for i in range(t):
    text=input()
    textArr=[]
    wordArr=[]
    for j in range(len(text)):
        textArr.append(text[j])
    word=input()
    for j in range(len(word)):
        wordArr.append(word[j])
    count(wordArr,textArr)