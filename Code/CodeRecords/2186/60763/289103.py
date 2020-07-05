def sum1(s):
    return int((s*(s+1)*(2*s+1)/6 + (s+1)*s/2)/2)

T = int(input())
for i in range(T):
    N = int(input())
    print(sum1(N))