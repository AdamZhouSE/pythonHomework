def test():
    n = int(input())
    matches = list(eval(input()))
    segList = []
    for match in matches:
        if not getSegList(segList, match):
            print('[]')
            return
    res = []
    for seg in segList:
        topology(res, seg)
    for i in range(0, n):
        if i not in res:
            res.append(i)
    print(res)


def getSegList(segList, match) -> bool:
    thisCourse = match[0]
    beforeCourse = match[1]
    if segList == []:
        segList.append([beforeCourse, thisCourse])
        return True
    else:
        for i in range(0, len(segList)):
            seg = list(segList[i])
            for j in range(0, len(seg)):
                for k in range(0,j):
                    if seg[k]==thisCourse and seg[j]==beforeCourse:
                        return False
            if seg[-1] == beforeCourse:
                seg.append(thisCourse)
                segList.pop(i)
                segList.insert(i,seg)
                return True
        segList.append([beforeCourse, thisCourse])
        return True


def topology(res, seg):
    ind = -1
    for i in range(0, len(seg)):
        if seg[i] in res:
            ind = res.index(seg[i]) + 1
            continue
        else:
            if ind == -1 or ind >= len(res):
                res.append(seg[i])
            else:
                res.insert(ind, seg[i])
                ind = ind + 1


test()
