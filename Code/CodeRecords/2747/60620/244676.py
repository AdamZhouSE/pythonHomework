beginWord=input()
endWord=input()
wordList=set(input())
result=[]
visited=set()
forward={beginWord:[[beginWord]]}
backward={endWord:[[endWord]]}
l=2
while forward:
    if len(forward) > len(backward):
        forward, backward = backward, forward
    temp = {}
    while forward:
        word, paths = forward.popitem() 
        visited.add(word)  
        for i in range(len(word)):
            for a in 'abcdefghijklmnopqrstuvwxyz':
                new = word[:i]+a+word[i+1:]  
                if new in backward:
                    if paths[0][0] == beginWord:
                        result.extend(fPath + bPath[::-1] for fPath in paths for bPath in backward[new])
                    else:
                        result.extend(bPath + fPath[::-1] for fPath in paths for bPath in backward[new])
                if new in wordList and new not in visited:
                    temp[new] = tmp.get(new, []) + [path + [new] for path in paths]
    l+= 1
    if result and _len > len(result[0]):
        break
    forward = temp
print(result)