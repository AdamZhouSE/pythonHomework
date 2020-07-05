def ar(ll):
    for l in ll:
        print((l[0]+1)//2*l[1])
if __name__ == '__main__':
    ar([[int(i) for i in input().split(' ')] for _ in range(int(input()))])
