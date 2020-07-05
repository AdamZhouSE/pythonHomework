
def add1(a: [int], l: int, r: int, k: int, d: int):
    distance = k
    for i in range(l-1, r):
        a[i] += distance
        distance += d


if __name__ == '__main__':

    x = input().strip().split()
    n = int(x[0])
    m = int(x[1])
    x = input().strip().split()
    a = []
    for i in x:
        a.append(int(i))

    ops = []
    for i in range(m):
        ops.append(input())

    for op in ops:
        o = op.strip().split()
        if o[0] == "1":
            add1(a, int(o[1]), int(o[2]), int(o[3]), int(o[4]))
            # print(a)
        else:
            oo = int(o[1])
            print(a[oo-1])
