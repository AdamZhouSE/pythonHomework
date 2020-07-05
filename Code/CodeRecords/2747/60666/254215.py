beginWord=input()
endWord=input()
wordList=eval(input())
wordList=set(wordList)
if endWord not in wordList:
    print([])
elif endWord==beginWord:
    print(1)
else:
    N,level=len(beginWord),1
    head,tail={beginWord},{endWord}
    wordList.remove(endWord)
    chars=set('abcdefghijklmnopqrstuvwxyz')
    while head and tail:
        if len(head)>len(tail):
            head,tail=tail,head
        s=set()
        while head:
            w=head.pop()
            for i in range(N):
                prefix,suffix=w[:i],w[i+1:]
                for c in chars:
                    nextWord=prefix+c+suffix
                    if nextWord in tail:
                        print(level+1)
                    else:
                        if nextWord in wordList:
                            s.add(nextWord)
                            wordList.remove(nextWord)
        head=s
        level+=1
    print([])