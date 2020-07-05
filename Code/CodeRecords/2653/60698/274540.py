def test():
    t = int(input())
    for _ in range(0, t):
        nx=input().split()
        n=int(nx[0])
        x=int(nx[1])
        if x>=10:
            print(0)
            return 
        else:
            time=10-x
            num=n-1
            print (num*time)



test()