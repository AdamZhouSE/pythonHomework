def j(n,l):
    m=min(l)
    for i in  l:
        if i%m!=0:
            print(-1)
            return
    print(m)
if __name__ == '__main__':
        j(int(input()),[int(i) for i in input().split(' ')])
    