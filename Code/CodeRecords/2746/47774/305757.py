begin=str(input())
end=str(input())
words=eval(input())

def solve(begin,end,words):
    wd=set(words)
    cur=[begin]
    nw=[]
    depth=1
    while cur:
        for word in cur:
            if word==end:
                return depth
            for index in range(len(word)):
                for indice in 'abcdefghijklmnopqrstuvwxyz':
                    new=word[:index]+indice+word[index+1:]
                    if new in wd:
                        wd.remove(new)
                        nw.append(new)
        depth+=1
        cur=nw
        nw=[]
    return 0

print(solve(begin,end,words))
            
        