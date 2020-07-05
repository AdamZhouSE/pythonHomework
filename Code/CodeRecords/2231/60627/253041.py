# 5
n = int(input())
for i in range(n):
    N = int(input())
    li = []
    while N != 1:
        for i in range(2,N+1):
            if N%i == 0:
                N = int(N/i)
                li.append(i)
                break
    if len(set(li)) == 3 and len(li) == 3:
        print(1)
    else:
        print(0)