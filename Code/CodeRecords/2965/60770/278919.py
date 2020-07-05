def solve():
    k=int(input().split()[0])
    src=input()
    total=int(input())
    ops=[]
    for _ in range(total):
        ops.append(list(map(int,input().split())))

    res=src
    for op in ops:
        res=res[:op[2]]+res[op[0]:op[1]]+res[op[2]:]

    out=res[:k]
    print(out,end='')

if  __name__ == '__main__' :
    solve()