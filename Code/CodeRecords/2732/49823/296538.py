def ej(l):
    for i in l:
        print((i[0]**i[1])%l[2])
if __name__ == '__main__':
    ej([[int(i) for i in input().split(' ')] for _ in range(int(input()))])
