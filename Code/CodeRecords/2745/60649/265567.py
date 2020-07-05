beginWord=input()
endWord=input()
wordList=set(eval(input()))
if endWord not in wordList:
    print([])
else:
    res=[]
    visited,front,back,lens=set(),{beginWord:[[beginWord]]},{endWord:[[endWord]]},2
    while front:
        if len(front)>len(back):
            front, back = back, front
        tmp={}
        while front:
            word,path=front.popitem()
            visited.add(word)
            for i in range(len(word)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    nword=word[:i]+j+word[i+1:]
                    if nword in back:
                        if path[0][0]==endWord:
                            res.extend(bp+fp[::-1] for fp in path for bp in back[nword])
                        else:
                            res.extend(fp+bp[::-1] for fp in path for bp in back[nword])
                    if nword in wordList and nword not in visited:
                        tmp[nword]=tmp.get(nword,[]+[p+[nword] for p in path])
        lens +=1
        if res and lens>len(res[0]):
            break
        front=tmp
    print(res)

