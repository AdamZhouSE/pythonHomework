import sys

def solve():
    srcli=sys.stdin.readlines()[:-1]
    src=''.join(srcli)
    res=''
    for s in src:
        res+=fanma(s)
    print(res)

def fanma(s):
    n=ord(s)
    if 97<=n<=122:
        n=219-n
    elif 64<=n<=90:
        n=154-n
    return chr(n)

if __name__ == '__main__':
    solve()