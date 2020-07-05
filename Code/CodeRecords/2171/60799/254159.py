T = int(input())
for ttt in range(T):
    n = int(input())
    nList = input().strip().split()
    res_0 = []
    res_1 = []
    [res_0.append(i) if int(i) % 2 == 0 else res_1.append(i) for i in nList]
    print(' '.join(res_0+res_1)+' ')