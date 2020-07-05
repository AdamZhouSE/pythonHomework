def manySort(numlst,sortlst):
    for i in range(len(sortlst)):
        type = sortlst[i][0]
        beg = sortlst[i][1]
        end = sortlst[i][2]
        temp = numlst[(beg-1):end]
        if type == 0:
            temp = sorted(temp)
        else:
            temp = sorted(temp,reverse=True)
        for j in range(beg-1,end):
            numlst[j] = temp[j-beg+1]
        #print(numlst)

if __name__ == "__main__":
    n,m = map(int,input().split(" "))
    numlst = list(map(int,input().split(" ")))
    sortlst = []
    for i in range(m):
        sortlst.append(list(map(int,input().split(" "))))
    manySort(numlst,sortlst)
    k = int(input())
    print(numlst[k-1])