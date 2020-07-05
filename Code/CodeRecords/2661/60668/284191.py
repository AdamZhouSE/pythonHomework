def linerlist_20_count(N):
    co_0=0
    co_1=0
    N=N[2:]
    for i in range(len(N)):
        if N[i]=='1':
            co_1+=1
        elif N[i]=='0':
            co_0+=1
    return co_0 ^ co_1
if __name__=='__main__':
    for _ in range(int(input())):
        N = input()
        print(linerlist_20_count(bin(int(N))))