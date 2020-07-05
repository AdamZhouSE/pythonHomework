test_num = int(input())
for i in range(test_num):
    line = input().split(" ")
    s = line[0]
    k = int(line[1])
    result = []
    if s.count("1") == k:
        sum = 1
    else:
        sum = 0
    for j in range(k,len(s)):
        for m in range(0,len(s)-j+1):
            if s[m:m+j].count("1") == k:
                sum += 1
                result.append(s[m:m+j])
    print(sum)
