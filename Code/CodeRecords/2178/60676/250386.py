# 魔咒串由许多魔咒字符组成，魔咒字符可以用数字表示。例如可以将魔咒字符1、2拼凑起来形成一个魔咒串[1,2]。
# 一个魔咒串S的非空子串被称为魔咒串S的生成魔咒。
# 例如S=[1,2,1]时，它的生成魔咒有[1]、[2]、[1,2]、[2,1]、[1,2,1]五种。S=[1,1,1]时，它的生成魔咒有[1]、[1,1]、[1,1,1]三种。
# 最初S为空串。共进行n次操作，每次操作是在S的结尾加入一个魔咒字符。每次操作后都需要求出，当前的魔咒串S共有多少种生成魔咒。


def substring(s):
    substrings = [s[0]]
    res = [1]
    for i in range(len(s)-1):
        if s[i+1] not in substrings:
            substrings.append(s[i+1])
        for j in range(i+1):
            new_substring = s[i+1]
            for k in range(i+1-j):
                new_substring = s[i-k] + new_substring
            if new_substring not in substrings:
                substrings.append(new_substring)
        res.append(len(substrings))
    return res


a = input()
result = substring(input().split())
for i in range(len(result)):
    print(result[i])