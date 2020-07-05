import math;

def getAns(n):
    i = 1;
    ans = 0;
    while i <= n:
        ans += math.pow(i, 5)
        i += 1;
    return int(ans);


if __name__ == '__main__':
    T = int(input());
    for i in range (T):
        N = int(input());
        print(getAns(N))