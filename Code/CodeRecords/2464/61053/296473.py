def minNum(numlst,s):
    i = 0
    temp = numlst[0]
    res = len(numlst)
    j = 1
    while j <= len(numlst):
        if temp >= s:
            res = min(j - i, res)
            i += 1
            temp -= numlst[i]
        else:
            if j >= len(numlst):
                break
            temp += numlst[j]
            j += 1
    return res

if __name__ == "__main__":
    k = int(input())
    numlst = list(map(int,input().split(',')))
    print(minNum(numlst,k))