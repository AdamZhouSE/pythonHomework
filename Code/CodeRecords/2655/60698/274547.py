from math import log

def test():
    t = int(input())
    for _ in range(0, t):
        n=int(input())
        log_n=log(n,2)
        if log_n%1==0:
            print(n)
        else:
            res=pow(2,int(log_n)+1)
            res=int(res)
            print(res)




test()