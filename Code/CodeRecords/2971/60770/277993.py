def solve():
    src=input()
    n=len(src)
    li=[]
    for i in range(n):
        li.append([src[i:],i+1])
    li.sort(key=lambda x:x[0])
    out=list(map(lambda x:str(x[1]),li))
    print(' '.join(out))

if __name__ == '__main__':
    solve()