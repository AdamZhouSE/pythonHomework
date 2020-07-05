def ToInt2(s):
    dicts = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}  # 准备好我们的字典
    results = 0
    for i in range(0, len(s)):  # 遍历要判断的字符串
        if i != len(s) - 1:  # 最后一个字符前要进行特殊规则的判断
            if dicts[s[i]] >= dicts[s[i + 1]]:
                results += dicts[s[i]]
            else:
                results -= dicts[s[i]]
        else:  # 直接加上最后一个罗马字符对应的值
            results += dicts[s[i]]
    return results

def toInt(a):
    if a == 'I':
        return 1
    elif a == 'V':
        return 5
    elif a == 'X':
        return 10
    elif a == 'L':
        return 50
    elif a == 'C':
        return 100
    elif a == 'D':
        return 500
    elif a == 'M':
        return 1000

def toInt1(b,a):
    if a == 'V':
        return 4
    elif a == 'X':
        return 9
    elif a == 'L':
        return 40
    elif a == 'C':
        return 90
    elif a == 'D':
        return 400
    elif a == 'M':
        return 900

str1 =input()
i = 0
count = 0
while i<len(str1):
    if i == len(str1)-1:
        count += toInt(str1[i])
        i +=1
    elif str1[i] == 'I' and str1[i+1]!= 'I':
        count += toInt1(str1[i],str1[i+1])
        i +=2
    else:
        count += toInt(str1[i])
        i +=1
# print(count)
print(ToInt2(str1))