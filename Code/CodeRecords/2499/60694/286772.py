N = int(input())
l = [-1]
cnt = 0
for _ in range(N):
    tmp = input().split()
    if tmp[0] == "Add":
        cnt += 1
        l.append(list(map(int, tmp[1:])) + [cnt])

    elif tmp[0] == "Del":
        for i in range(len(l)):
            if l[i] != -1:
                if int(tmp[1]) == l[i][3]:
                    del l[i]
                    break

    elif tmp[0] == "Query":
        x = int(tmp[1])
        ans = 0
        for ele in l:
            if ele != -1:
                if ele[0] * x + ele[1] > ele[2]:
                    ans += 1
        print(ans)

