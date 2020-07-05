tree = {'':0}


def insert(word):
    tree[word]=1

def delete(word):
    if word in tree:
        tree[word]-=1
        if tree[word]==0:
            del tree[word]

def search(word):
    return word in tree

def prefix_number(pre):
    l=len(pre)
    res=0
    for word in tree:
        if word[0:l]==pre:
            res+=1
    return res
tests = int(input())
for t in range(tests):
    req = input().split()
    cmd = int(req[0])
    word=req[1]
    if cmd==1:
        insert(word)
    elif cmd==2:
        delete(word)
    elif cmd==3:
        if search(word):
            print('YES')
        else:
            print('NO')
    else:
        print(prefix_number(word))