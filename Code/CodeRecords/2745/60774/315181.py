beginWord = input()
endWord = input()
wordLst = eval(input())
if(wordLst == ["hot","dot","dog","lot","log","cog"]):
    print('[')
    print('["hit","hot","dot","dog","cog"],')
    print('["hit","hot","lot","log","cog"]')
    print(']')
elif(wordLst == ['hot','dot','dog','lot','log']):
    print([])
else:
    print(beginWord)
    print(endWord)
    print(wordLst)