import bisect

if __name__ == '__main__':
    x = input().strip().split()
    n = int(x[0])
    m = int(x[1])
    infos = []
    for i in range(m):
        infos.append(input())
    destroied = []
    for info in infos:
        if info[0] == "D":
            destroied.append(int(info[2:]))
        elif info[0] == "R":
            destroied.pop()
        else:
            ss = destroied.copy()
            ss.sort()
            pos = int(info[2:])
            ss.insert(0, 0)
            ss.append(n+1)
            l = 0
            r = n+1
            for i in range(0, len(ss)-1):
                if ss[i] <= pos <= ss[i+1]:
                    l = ss[i]
                    r = ss[i+1]
            print(r-l-1)
