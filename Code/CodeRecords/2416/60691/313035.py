def findMax(stu:list):
    maxlen = 0
    i = 0
    j = 1
    num = len(stu)
    nowlen = 1
    while j != num+1:

        if j<num and stu[i] != stu[j]:
            nowlen = nowlen + 1
        else:
            maxlen = max(maxlen,nowlen)
            nowlen = 1
        i = i + 1
        j = j + 1
    return maxlen
    pass

line = input().split(' ')
N = int(line[0])
M = int(line[1])
stu = [1]*N
re = []
for i in range(M):
    n = int(input())
    if stu[n-1] == 1:
        stu[n-1] = 0
    else:stu[n-1] = 1
    re.append(findMax(stu))
for i in re:
    print(i)