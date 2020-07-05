from functools import reduce


def solve():
    n=int(input())

    def numMul(num):
        num=list(map(int,list(str(num))))
        res=reduce(lambda x,y:x*y,num)
        return res

    def getAllNum(numstr):
        total=len(numstr)
        res=[]
        for i in range(1,total+1):
            for j in range(total+1-i):
                res.append(int(numstr[j:j+i]))
        return res

    for i in range(n):
        num=input()
        childNum=getAllNum(num)
        mulLi=list(map(numMul,childNum))
        s=set(mulLi)
        if len(s)==len(mulLi):
            print(1)
        else:
            print(0)

if  __name__ == '__main__' :
    solve()