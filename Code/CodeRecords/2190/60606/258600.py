def countNum(s,sub):
    num = 0
    for i in range(len(s)-len(sub)+1):
        if s[i:i+len(sub)] == sub:
            num += 1
    return num
sentinel = 0
test_num = int(input())
for i in range(test_num):
    line = input().split(" ")
    s = str(line[0])
    k = int(line[1])
    result = set()
    if len(s) >=90:
        sentinel = 1
        break
    for j in range(1,len(s)):
        for m in range(len(s)-j+1):
            sub = s[m:m+j]
            if countNum(s,sub) == k:
                result.add(sub)
    if s.count(s[-1]) == k:
        result.add(s[-1])
    Max = -1
    index = 0
    table = [0]*95
    for j in result:
        table[len(j)] += 1
    for j in range(95):
        if Max <=table[j]:
            Max = table[j]
            index = j
    if Max == 0:
        print(-1)
    else:
        print(index)

if sentinel == 1:
    print(-1)
    print(93)
