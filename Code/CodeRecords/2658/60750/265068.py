

def solve():
    test = int(input())
    res = []
    for i in range(0,test):
        line1 = list(map(int,input().split(' ')))
        line2 = list(map(int, input().split(' ')))
        n = line1[0]
        x = line1[1]
        tmp = []
        computed = 0
        for j in range(0,n):
            if line2[j] % x == 0:
                tmp.append(line2[j])
        for j in range(0,len(tmp)):
            computed = computed | tmp[j]
        res.append(computed)

    for i in range(0,test):
        print(res[i])

solve()