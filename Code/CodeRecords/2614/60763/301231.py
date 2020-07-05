T = int(input())
for i in range(T):
    N = int(input())
    s = []
    for j in range(3):
        s.append(list(map(int,(""+input()).split(' '))))
    # print(s)
    count = 0
    for j in range(N):
        for k in range(N):
            if s[2][k] == s[0][j] - s[1][j]:
                count += 1
    print(count)