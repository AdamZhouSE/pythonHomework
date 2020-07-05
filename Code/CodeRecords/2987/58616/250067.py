def reverseStr(s):
    revS = ''
    # 基于对象的for循环中，逆序地遍历元素
    for ch in s[::-1]:
        revS += ch
    return revS


testStr = input()
print(testStr + reverseStr(testStr))