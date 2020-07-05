def left_scan(numlst,N):
    left_max = [0]
    max_height = numlst[0]
    for i in range(1,N):
        if numlst[i] > max_height:
            max_height = numlst[i]
        left_max.append(max_height)
    return left_max

def right_scan(numlst,N):
    right_max = [0]
    max_height = numlst[N-1]
    for i in range(N-2,-1, -1):
        if numlst[i] > max_height:
            max_height = numlst[i]
        right_max.append(max_height)
    return right_max[::-1]

def max_rain(numlst,N):
    L_max = left_scan(numlst,N)
    R_max = right_scan(numlst,N)
    sum = 0
    for i in range(1,N-1):
        ith_rain = min(L_max[i],R_max[i]) - numlst[i]
        if ith_rain > 0:
            sum = sum + ith_rain
    return sum


if __name__ == "__main__":
    testNO = int(input())
    res = []
    for i in range(0,testNO):
        N = int(input())
        numlst = list(map(int,input().split()))
        res.append(max_rain(numlst,N))
    for i in res:
        print(i)