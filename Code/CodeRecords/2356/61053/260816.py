def find_v(numlst):
    record = []
    maxval = numlst[0]
    for i in range(0,len(numlst)):
        if numlst[i] > maxval:
            maxval = numlst[i]
        lst = [maxval]
        record.append(lst)

    minval = numlst[len(numlst)-1]
    for i in range(len(numlst)-1,-1,-1):
        if numlst[i] < minval:
            minval = numlst[i]
        record[i].append(minval)

    for i in range(1,len(numlst)-1):
        if numlst[i] >= record[i][0] and numlst[i] <= record[i][1]:
            return numlst[i]
    return -1

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(0,testNO):
        N = int(input())
        numlst = list(map(int,input().split()))
        ans.append(find_v(numlst))
    for no in ans:
        print(no)