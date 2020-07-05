# https://zhuanlan.zhihu.com/p/76887442

def solve():
    n=int(input())
    ghosts=[]
    for i in range(n):
        ghosts.append(tuple(map(int,input().split(','))))
    target=tuple(map(int,input().split(',')))
    d1=abs(target[0])+abs(target[1])
    d2=float('inf')
    for ghost in ghosts:
        d2 = abs(ghost[0]-target[0])+abs(ghost[1]-target[1])
        if d2<=d1:
            print("False")
            return 
    print("True")
    
if  __name__ == '__main__' :
    solve()