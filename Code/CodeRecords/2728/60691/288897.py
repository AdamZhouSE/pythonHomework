import itertools

import itertools


def function(s):
    l = []
    for i in range(len(s)):
        if s[i].isalnum():
            l.append(int(s[i]))

    num = []
    result = []
    for i in range(len(l)):
        num.append(i)

    temp = list(itertools.combinations(num, 2))

    for i in range(len(temp)):
        tempnum = list(temp[i])
        result.append(abs(tempnum[0] - tempnum[1]) * min(l[tempnum[0]], l[tempnum[1]]))

    return max(result)


n =int(input())
nums = []
string = []

for i in range(n):
    nums.append(input())
    string.append(input())

for i in range(n):
    print(function(string[i]))








