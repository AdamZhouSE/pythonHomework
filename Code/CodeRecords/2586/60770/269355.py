def solve():
    a=int(input())
    b=int(input())
    c=int(input())
    xyz=[a,b,c]
    xyz.sort()
    res=[1,0]
    if xyz[2]-xyz[0]==2:
        res[0]=0
    elif xyz[0]+2<xyz[1] and xyz[1]+2<xyz[2]:
        res[0]=2
    res[1]=xyz[2]-xyz[0]-2
    print(res)

if  __name__ == '__main__' :
    solve()