if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        a = input().split()
        st = set(a)
        d = {}
        for item in st:
            d[item] = a.count(item)
        dl = sorted(d.items(), key=lambda x: x[0])
        dll = sorted(dl, key=lambda x: x[1], reverse=True)
        print(dll[0][0],end=' ')
        print(dll[0][1])
