tests = int(input())
for i in range(0,tests):
    N = int(input())
    i = 1
    res = 0
    while i<=N:
        res+=pow(N-i+1,2)
        i+=1
    print(res)