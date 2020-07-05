def solve(num,t):
    n=list(map(int,num))
    if n.count(t)!=0:
        return n.index(t)
    n.append(t)
    n.sort()
    return n.index(t)
if __name__ == '__main__':
    num=eval(input())
    t=int(input())
    print(solve(num,t))