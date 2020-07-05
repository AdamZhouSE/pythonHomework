def insert(intervals, newInterval):
    if len(intervals) == 0:
        return [newInterval]
    res = []
    temp = intervals+[newInterval]
    temp = list(sorted(temp))
    low = temp[0][0]
    high = temp[0][1]
    for i in range(1,len(temp)):
        if high >= temp[i][0]:
            if high < temp[i][1]:
                high = temp[i][1]
        else:
            res.append([low,high])
            low = temp[i][0]
            high = temp[i][1]
    res.append([low,high])
    return res


if __name__ == '__main__':
    num=eval(input())
    new_num=eval(input())
    result=insert(num,new_num)
    print(result)
