
def solve():
    s1 = input().split(' ')
    n = int(s1[0])
    m = int(s1[1])
    data = list(map(int,input().split(' ')))
    for i in range(0,m):
        request = list(map(int,input().split(' ')))
        op = request[0]
        l = int(request[1])
        r = int(request[2])
        if op == 0:
            if l == 1:
                if r == n:
                    data.sort()
                else:
                    data = sorted(data[l - 1: r]) + data[r:]
            else:
                if r == n:
                    data = data[:l - 1] + sorted(data[l - 1: r])
                else:
                    data = data[:l - 1] + sorted(data[l - 1: r]) + data[r:]
        else:
            if l == 1:
                if r == n:
                    data.sort(reverse=True)
                else:
                    data = sorted(data[l - 1: r],reverse=True) + data[r:]
            else:
                if r == n:
                    data = data[:l - 1] + sorted(data[l - 1: r],reverse=True)
                else:
                    data = data[:l - 1] + sorted(data[l - 1: r],reverse=True) + data[r:]
    q = int(input())
    print(data[q -1])

solve()