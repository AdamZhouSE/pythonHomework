def getAns(N) -> str:
    bit = N // 10
    # if bit == 1:
    #     return 'N' + '0' * N
    return str(N - 9 * bit)+'9'*bit + '0' * N


T = eval(input())
for i in range(T):
    N = eval(input())
    print(getAns(N))
