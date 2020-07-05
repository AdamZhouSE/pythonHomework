def test():
    t = int(input())
    for _ in range(0, t):
        ab=input().split()
        ab=list(map(int,ab))
        a=ab[0]
        b=ab[1]
        lis=[]
        lower=0
        for i in range(1,b+1):
            lower=lower+i
        if a<lower:
            print(0)
        else:
            print(1)
            
    

test()