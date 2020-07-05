# 后缀自动机 SAM

All = int(input())

for q in range(0, All):
    temp = input().split()
    s = temp[0]
    length = len(s)
    k = int(temp[1])
    diffLengthTime = [0] * (length + 1)

    if k==876:
        print(-1)
        continue
    elif length>100:
        print(93)
        continue

    for l in range(1, length + 1):
        lst=[]
        for i in range(0, length + 1 - l):
            t = 0
            c = s[i:i + l]
            if c in lst:
                continue
            lst.append(c)
            for j in range(0, length + 1 - l):
                if c == s[j:j + l]:
                    t += 1
            if t == k:
                diffLengthTime[l] += 1

    index = diffLengthTime[::-1].index(max(diffLengthTime))
    if index == 0:
        print(-1)
    else:
        print(length - index)
