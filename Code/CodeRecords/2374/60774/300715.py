t = int(input())
for i in range(0,t):
    n = int(input())
    numLst = list(map(int,input().split(' ')))
    numSet = set(numLst)
    record = []
    for num in numSet:
        record.append([num,numLst.count(num)])
    record.sort(key = lambda x:(-x[1],x[0]))
    s = ''
    for item in record:
        s = s + (str(item[0]) + ' ') * item[1]
    print(s)