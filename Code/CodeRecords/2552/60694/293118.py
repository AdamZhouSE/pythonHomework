N, M = map(int, input().split())
mines = [[] for _ in range(N)]
type = 1
for _ in range(M):
    Q, L, R = map(int, input().split())
    if Q == 1:
        for i in range(L-1, R):
            mines[i].append(type)
        type += 1
    elif Q == 2:
        ans = []
        for i in range(L-1, R):
            for ele in mines[i]:
                if ele not in ans:
                    ans.append(ele)
        print(len(ans))

