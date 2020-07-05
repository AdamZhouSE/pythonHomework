def findMin(numlst):
    minVal = numlst[0]
    for no in numlst:
        if no < minVal:
            minVal = no
    return minVal

if __name__ == "__main__":
    numlst = list(map(int,input().split(',')))
    print(findMin(numlst))