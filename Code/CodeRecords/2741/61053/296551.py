def maxUp(numlst):
    i = 1
    res = 1
    count = 1
    while i < len(numlst):
        if numlst[i] > numlst[i-1]:
            count += 1

        else:
            res = max(res,count)
            count = 1
        i += 1
    return res

if __name__ == "__main__":
    lst = eval(input())
    print(maxUp(lst))