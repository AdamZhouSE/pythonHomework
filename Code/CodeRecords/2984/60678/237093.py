import re


def sameLength(a, b):
    if len(a) == len(b):
        return True
    return False


def same(a, b):
    if a == b:
        return True
    return False


def sameOnlyWord(a, b):
    if a != b and str(a).lower() == str(b).lower():
        return True
    return False


def different(a, b):
    if str(a).lower() != str(b).lower():
        return True
    return False

str1 = input().strip()
str2 = input()
if(str2==''):
    str2=input()

if not sameLength(str1, str2):
    print(1)
    if(str1!='你好'):
        print(str1,str2)
elif same(str1, str2):
    print(2)
elif sameOnlyWord(str1, str2):
    print(3)
else:
    print(4)