t = int(input())
count = 0
res = []
arr = [-1 for x in range(1000)]
b = set()


def get_arr(num, m, n):
    global count
    global res
    for k in range(num, m + 1):
        if num <= m:
            res.append(k)
            if len(res) == n:
                s = ''
                for j in res:
                    s += str(j)
                b.add(s)
            if len(res) < n:
                get_arr(2 * k, m, n)
            del res[-1]


for i in range(t):
    tmp = input()
    tmp = [int(k) for k in tmp.split(" ")]
    m = tmp[0]
    n = tmp[1]
    count = 0
    res = []
    b = set()
    get_arr(1, m, n)
    print(len(b))
