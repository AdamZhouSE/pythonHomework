def solve():
    txt=''
    hst=['']
    n=int(input())
    for i in range(n):
        op=input().split()
        if op[0]=='T':
            txt+=op[1]
            hst.append(txt)
        elif op[0]=='Q':
            print(txt[int(op[1])-1])
        elif op[0]=='U':
            steps=int(op[1])
            hst=hst[:-steps]
            txt=hst[len(hst)-1]

if  __name__ == '__main__' :
    solve()