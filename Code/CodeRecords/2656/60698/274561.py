from math import log

def test():
    t = int(input())
    for _ in range(0, t):
        mn=input().split()
        m=int(mn[0])
        n=int(mn[1])
        bin_m=bin(m)[2:]
        bin_n=bin(n)[2:]
        if m==n:
            print(-1)
        else:
            while len(bin_m)<len(bin_n):
                bin_m='0'+bin_m
            while len(bin_m)>len(bin_n):
                bin_n='0'+bin_n
            index=0
            for i in range(len(bin_n)-1,-1,-1):
                if bin_n[i]!=bin_m[i]:
                    index=i
                    break
            res=len(bin_n)-index
            print(res)
test()
