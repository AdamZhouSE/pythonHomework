def combination(intervals):
    merged=[]
    intervals.sort(key=lambda tple:tple[0])
    for interval in intervals:
        if not merged or merged[-1][1]<interval[0]:
            merged.append(interval)
        else:
            merged[-1][1]=max(merged[-1][1],interval[1])
    return merged
lstStr=input()
intervals=eval(lstStr)
def printList(list):
    print('[',end='')
    firstFlag=False
    for lst in list:
        if not firstFlag:
            firstFlag=True
            print('[{},{}]'.format(lst[0],lst[1]),end='')
        else:
            print(',[{},{}]'.format(lst[0],lst[1]),end='')
    print(']')
print(combination(intervals))