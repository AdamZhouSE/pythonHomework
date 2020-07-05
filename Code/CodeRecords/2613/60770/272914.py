def solve():
    n=int(input())

    def solveOne():
        des=int(input())
        c1,c2,cur=0,0,0
        res=[]
        while c1<des:
            cur+=1
            res.append(cur)
            c1+=1
            if c1==des:
                return res
            for i in range(c2):
                cur+=2
                res.append(cur)
                c1+=1
                if c1==des:
                    return res
            c2+=1
        return res

    for i in range(n):
        res=solveOne()
        res=list(map(str,res))
        print(' '.join(res))

if  __name__ == '__main__' :
    solve()