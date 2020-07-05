'''
有一个名为Vijay的黑客，他开发了一种方法，可以使用其用户名来检查某个社交网站上的ID是虚假的还是真实的。 他的方法包括：如果用户名中不同字符的数量为奇数，则该用户为男性，否则为女性。系统会为您提供表示用户名的字符串，请帮助Vijay通过其方法确定该用户的性别。忽略元音。
'''


def isIn(c, rmv):
    for i in range(0, len(rmv)):
        if c == rmv[i]:
            return True
    return False


def isVowel(c):
    vowel = ['a', 'e', 'i', 'o', 'u']
    if isIn(c, vowel):
        return True
    return False


def difStr(s):
    rmv = []
    for i in range(0, len(s)):
        if isVowel(s[i]):
            continue
        if isIn(s[i], rmv):
            continue
        else:
            rmv.append(s[i])
    length = len(rmv)
    if length % 2 == 0:
        print('SHE!')
    else:
        print('HE!')


n = int(input())
for i in range(0, n):
    s = str(input())
    difStr(s)