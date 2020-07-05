import string


def ispalindrome(src):
    l = len(src)
    if l<=1:
        return True
    return src[0]==src[l-1] and ispalindrome(src[1:l-1])


num=int(input())
for i in range(num):
    src=input()
    tar=''.join([c for c in src if c not in string.punctuation])
    tar=tar.replace(' ', '')
    tar=tar.lower()
    if ispalindrome(tar):
        print("YES")
    else:
        print("NO")