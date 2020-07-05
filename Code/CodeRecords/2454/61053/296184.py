def findMin(numlst):
    low = 0
    high = len(numlst) - 1
    while low < high:
        if numlst[low] < numlst[high]:
            return numlst[low]
        mid = int((low+high)/2)
        if numlst[mid] > numlst[low]:
            low = mid
        else:
            high = mid
    return min(numlst[low+1],numlst[low])

if __name__ == "__main__":
    numlst = list(map(int,input().split(',')))
    print(findMin(numlst))