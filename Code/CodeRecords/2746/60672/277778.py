import sys
beginword=input()
endword=input()
fakelist=input()
alpha='abcdefghijklmnopqrstuvwxyz'
l=len(beginword)
wordlist=[]
for i in range(len(fakelist)):
    if fakelist[i] in alpha and fakelist[i+1] in alpha and fakelist[i+2] in alpha:
        wordlist.append(fakelist[i:i+l])
def search(beginword,endword,wordlist):
    if endword not in wordlist:
        return 0
    wordset=set(wordlist)
    length=1
    q=[beginword,]
    while len(q)!=0:
        k=len(q)
        for n in range(k):
            word=q.pop(0)
            if word==endword:
                return length
            for i in range(len(word)):
                newword=word
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    newword=word[:i]+c+word[i+1:]
                    if newword in wordset and newword!=word:
                        q.append(newword)
                        wordset.remove(newword)
        length+=1
    return length

length=search(beginword,endword,wordlist)

print(length)