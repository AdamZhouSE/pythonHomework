t = int(input())
count = 0
res = []


def get_arr(num, m, n):
    global count
    global res
    for k in range(num, m):
        if num * 2 <= m:
            res.append(num)
            if len(res) < n:
                get_arr(2 * num, m, n)
            if len(res) == n:
                count += 1
            del res[-1]


for i in range(t):
    tmp = input()
    tmp = [int(k) for k in tmp.split(" ")]
    m = tmp[0]
    n = tmp[1]
    count = 0
    res = []
    get_arr(1, m, n)
    print(count)
