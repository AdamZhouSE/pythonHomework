def solve():
    letters=list('abcdefghijklmnopqrstuvwxyz')
    disjointset=[-1 for i in range(26)]
    def rootOf(letter):
        nonlocal letters
        nonlocal disjointset
        index=letters.index(letter)
        if disjointset[index]==-1:
            return letter
        else:
            return rootOf(letters[disjointset[index]])
    def isEqual(a,b):
        root1=rootOf(a)
        root2=rootOf(b)
        if root1==root2:
            return True
        else:
            return False
    def join(a,b):
        if isEqual(a,b):
            return
        root1=rootOf(a)
        root2=rootOf(b)
        disjointset[letters.index(root1)]=letters.index(root2)

    src=input()[1:-1].replace('"','').split(',')
    equals,conflicts=[],[]
    for s in src:
        if s[1]=='=':
            equals.append([s[0],s[3]])
        else:
            conflicts.append([s[0],s[3]])
    for e in equals:
        join(e[0],e[1])
    for c in conflicts:
        if isEqual(c[0],c[1]):
            return False
    return True

if  __name__ == '__main__' :
    if solve():
        print('true')
    else:
        print('false')