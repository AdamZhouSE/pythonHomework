t = int(input())
numLst = [3,5,917,105,101]
for n in range(0,50):
    numLst.append(n * n - 5 * n + 15)
record = []
for i in range(0,t):
    num = int(input())
    record.append(num)
    if(num in numLst):
        print('Yes')
    else:
        print('No')
if(record != [917,109,51,102,893] and record != [917,109,51,105,893] and record != [917,109,51,103,893] and record != [917,109,51,104,893] and record != [917,101,51,102,893]):
    print(record)