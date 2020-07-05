def divideBlock(numlst):
    count = 0
    maxval = numlst[0]
    for i in range(len(numlst)):
        if numlst[i] > maxval:
            maxval = numlst[i]
        if maxval == i:
            count += 1
            
    return count

if __name__ == "__main__":
    numlst = eval(input())
    res = divideBlock(numlst)
    print(res)