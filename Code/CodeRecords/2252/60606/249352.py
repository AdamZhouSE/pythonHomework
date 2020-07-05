def countNum(s,j):
    num = 0
    for i in range(0,len(s) - len(j)+1):
        if s[0+i:i+len(j)] == j:
            num += 1
    return num
def permutation(s):
    result = []
    if len(s) == 1:
        result.append(s)
        return result
    else:
        for i in range(len(s)):
            for item in permutation(s[:i]+s[i+1:]):
                result.append(s[i] + str(item))
        return result

test_num = int(input())
for i in range(test_num):
    s = input()
    target = input()
    num = 0
    result = permutation(target)
    set1 = set()
    for j in result:
        set1.add(j)
    for j in set1:
        num += countNum(s,j)
    print(num)
