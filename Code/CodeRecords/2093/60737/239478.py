def get_perm(n, k):
    dict = [0]*(n+1)
    res = ''
    cand = []
    dict[0] = 1
    d = 1
    for i in range(1, n+1):
        cand.append(i)
        d *= i
        dict[i] = d
    k -= 1
    while n>0:
        index = k // dict[n-1]
        res += str(cand.pop(index))
        k -= index*dict[n-1]
        n -= 1
    return res


if __name__ == "__main__":
    n = int(input())
    k = int(input())
    print(get_perm(n, k))
