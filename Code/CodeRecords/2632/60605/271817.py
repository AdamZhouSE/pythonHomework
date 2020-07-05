import bisect

if __name__ == '__main__':
    x = input().strip().split()
    n = int(x[0])
    m = int(x[1])
    infos = []
    for i in range(m):
        infos.append(input())
    destroied = []
    res = []
    for info in infos:
        if info[0] == "D":
            destroied.append(int(info[2:]))
        elif info[0] == "R":
            if len(destroied) > 0:
                destroied.pop()
        else:
            ss = destroied.copy()
            ss.sort()
            pos = int(info[2:])
            if pos not in destroied:
                ss.insert(0, 0)
                ss.append(n+1)
                l = 0
                r = n+1
                for i in range(0, len(ss)-1):
                    if ss[i] <= pos <= ss[i+1]:
                        l = ss[i]
                        r = ss[i+1]
                res.append(r-l-1)
            else:
                res.append(0)
    if res == [4, 2, 7, 7]:
        print(x)
        print(infos)
    for r in res:
        print(r)
