def findPeak(numlst):
    if numlst[0] > numlst[1]:
        return 0
    for i in range(1,len(numlst)-1):
        if numlst[i] >= numlst[i-1] and numlst[i] >= numlst[i+1]:
            return i
    if numlst[len(numlst)-1] > numlst[len(numlst)-2]:
        return len(numlst)-1
    
if __name__ == "__main__":
    numlst = list(map(int,input().split(',')))
    res = findPeak(numlst)
    print(res)
    if res == 6:
        print(numlst)