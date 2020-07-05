def find_duplicate(n,numlst):
    low = 1
    high = n
    while low < high:
        mid = int((low + high) / 2)
        count = 0
        for no in numlst:
            if no <= mid:
                count += 1
        if count > mid:
            high = mid
        else:
            low = mid + 1
    return low

if __name__ == "__main__":
    numlst = list(map(int,input().split(',')))
    res = find_duplicate(len(numlst)-1,numlst)
    print(res)