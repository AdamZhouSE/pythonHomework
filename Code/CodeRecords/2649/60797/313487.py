if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        [n, l, r] = [int(a) for a in input().split()]
        bs = bin(n)
        bs = bs[2:]
        bs = list(bs)
        for i in range(len(bs)):
            c = bs[i]
            if len(bs)-r<=i<=len(bs)-l:
                if c=='1':
                    bs[i]='0'
                else:
                    bs[i]='1'
        bs = ''.join(bs)
        bs = '0b'+bs
        n = int(bs)
        print(n)