l = sorted(list(map(int, input().split(","))))
record = []
hasOne = False
if l[0] == 1:
    hasOne = True
    l.pop(0)
while len(l) != 0:
    tempArr = [l.pop(0)]
    copy = l.copy()
    for item in copy:
        if item % tempArr[-1]==0:
            tempArr.append(item)
            l.remove(item)
    if len(tempArr)>len(record):
        record = tempArr
if hasOne:
    record = [1]+record
print(record)
