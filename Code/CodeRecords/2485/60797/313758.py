if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        a = input().split()
        for item in a:
            item = set(item)
        d = {}
        for item in a:
            d[item] = a.count(item)

        dl = sorted(d.items(), key=lambda x: x[1])
        res = []

        for item in dl:
            res.append(len(item[0]))
        for i in range(len(res)):
            if i!=len(res)-1:
                print(res[i], end=' ')
            else:
                print(res[i])
