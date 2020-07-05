def ar(ll):
    for l in ll:
        a,b=0,0
        for i in range(len(l)):
            a+=l[i] if i%2==0 else 0
            b+=l[i] if i%2==1 else 0
        print(max(a,b))
if __name__ == '__main__':
    ar([[int(i) for i in input().split(' ')] for _ in range(int(input()))])
