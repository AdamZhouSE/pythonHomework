def test():
    t = int(input())
    for _ in range(0, t):
        xg=input().split()
        x=int(xg[0])
        g=int(xg[1])
        print(g-x-1)
        
test()