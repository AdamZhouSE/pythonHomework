def findMin(numlst):
    low = 0
    high = len(numlst) - 1
    while low < high:
        mid = int((low+high)/2)
        if mid > low:
            low = mid
        else:
            high = mid
    print(numlst[low])
if __name__ == "__main__":
    numlst = list(map(int,input().split(',')))
    findMin(numlst)