import sys


def solve():
    txt=sys.stdin.readlines()
    txt=list(map(lambda x:x.strip('\n'),txt))
    src=[]
    n=txt.count('9')
    for i in range(n):
        p=txt.index('9')
        src.append(txt[:p])
        txt=txt[p+1:]

    for i in range(n):
        cur=src[i]
        if isOk(cur):
            print('Set %d is not immediately decodable'% (i+1))
        else:
            print('Set %d is immediately decodable' % (i+1))


def isOk(li):
    m=len(li)
    for j in range(m):
        for k in range(m):
            if j == k:
                continue
            if li[j].startswith(li[k]):
                return True
    return False

if __name__ == '__main__':
    solve()
