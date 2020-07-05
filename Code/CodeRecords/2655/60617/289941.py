def power2():
    N=int(input())
    for i in range(0, 32):
        if 2**i>=N:
            print(2**i)
            return

if __name__=='__main__':
    T=int(input())
    for i in range(0,T):
        power2()