def countNum(s):
    set1 = set()
    for i in range(len(s)):
        set1.add(s[i])
    return len(set1)

test_num = int(input())
for i in range(test_num):
    s = input()
    n = int(input())
    max = -1
    if countNum(s) == n:
        max = len(s)
    for j in range(n,len(s)):
        for k in range(len(s)-j+1):
            if countNum(s[k:k+j]) == n and len(s[k:k+j]) > max:
                max = len(s[k:k+j])
    print(max)


