import math
def mmax(a, b):
    global Len
    for i in range(0, max(Len[a], Len[b])):
        A = word[a][i].upper()
        B = word[b][i].upper()
        if A == B:
            continue
        if A > B:
            return a
        else:
            return b
    return max(a, b)


if __name__ == '__main__':
    n, m = map(int, input().split(' '))
    word = [""]
    Len = [0]*1000
    maxn = [[0]*20 for i in range(0, 1000)]
    for i in range(0, n):
        word.append(input())
        Len[i+1] = len(word[i+1])
    for i in range(1, n+1):
        maxn[i][0] = i
    for j in range(1, 21):
        for i in range(1, n+1):
            if i+(1<<j)-1 <= n:
                maxn[i][j] = mmax(maxn[i][j-1], maxn[i+(1<<(j-1))][j-1])
    for i in range(0, m):
        l, r = map(int, input().split(' '))
        logn = int(math.log((r-l+1)/math.log(2.0)))
        index = mmax(maxn[l][logn], maxn[r-(1<<logn)+1][logn])
        print(word[index])