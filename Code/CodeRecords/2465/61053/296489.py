def findH(numlst):
    i = len(numlst) - 1
    while i >= 0:
        while i!=0 and numlst[i] == numlst[i-1]:
            i -= 1
        if numlst[i] <= len(numlst) - i:
            break
        i -= 1
    return numlst[i]

if __name__ == "__main__":
    numlst = list(map(int,input().split(',')))
    print(findH(numlst))