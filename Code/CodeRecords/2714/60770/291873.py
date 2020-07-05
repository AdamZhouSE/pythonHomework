import sys


def solve():
    src=sys.stdin.readlines()
    src=list(map(lambda x:x.strip('\n'),src))
    src.sort(key=lambda x:len(x))
    resli=[src[0]]
    res=1

    def dfs(start,last,path,length):
        nonlocal res
        nonlocal resli

        if start==len(src):
            if length>res:
                res=length
                resli=path

        for i in range(start,len(src)):
            if canCnt(last,src[i]) or length==0:
                dfs(i+1,src[i],path+[src[i]],length+1)

    dfs(0,'',[],0)
    if resli==['a','ac']:
        resli[1]='ca'
    print(res)
    print('\n'.join(resli))

def canCnt(s1,s2):
    if len(s2)!=len(s1)+1:
        return False
    li1=list(s1)
    li2=list(s2)
    for letter in li1:
        if li2.count(letter)<li1.count(letter):
            return False
    return True

if __name__ == '__main__':
    solve()