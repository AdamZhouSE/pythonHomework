T = int(input())
for i in range(T):
    N = int(input())
    s =  list(map(int,(''+input()).split(' ')))
    count = 0
    for i in range(N):
        for j in range(N):
            if j != i:
                for k in range(N):
                    if k!=j and s[i] == s[j] + s[k]:
                        count +=1
    if count == 0:
        print(-1)
    else:
        print(int(count/2))