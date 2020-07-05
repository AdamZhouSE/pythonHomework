def solve():
    n=int(input())
    mts=[]
    for _ in range(n):
        op=input().split()
        if op[0]=='A':
            mt=[int(op[1]),int(op[2])]
            res=0
            newmts=[]
            for m in mts:
                if isConflict(m,mt):
                    res+=1
                else:
                    newmts+=[m]
            newmts+=[mt]
            mts=newmts
            print(res)
        elif op[0]=='B':
            print(len(mts))

def isConflict(mt1,mt2):
    if mt1[0]>mt2[1] or mt2[0]>mt1[1]:
        return False
    return True

if __name__ == '__main__':
    solve()