def solve():
    m,n=int(input()),int(input())
    total=int(input())
    ops=[]
    for i in range(total):
        ops.append(list(map(int,input().split(','))))
    x=min(map(lambda x:x[0],ops))
    y=min(map(lambda x:x[1],ops))
    print(x*y)

if  __name__ == '__main__' :
    solve()