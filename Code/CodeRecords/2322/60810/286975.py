'''
如果一个正整数自身是回文数，而且它也是一个回文数的平方，那么我们称这个数为超级回文数。
现在，给定两个正整数 L 和 R （以字符串形式表示），返回包含在范围 [L, R] 中的超级回文数的数目。
'''


def isPalindrome(a):
    if a < 10:
        return True
    string = []
    while a > 0:
        temp = a % 10
        string.append(temp)
        a //= 10
    length = len(string)
    for i in range(0, length // 2 + 1):
        if string[i] != string[length - 1 - i]:
            return False
    return True


L = int(input())
R = int(input())
sqrtL = int(pow(L, 0.5))
sqrtR = int(pow(R, 0.5))
count = 0
for i in range(sqrtL, sqrtR+1):
    if isPalindrome(i) and isPalindrome(pow(i, 2)):
        count += 1
print(count)