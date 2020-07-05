def isHuiWen(str1):
    for i in range(0,len(str1)):
        if str1[i]!=str1[len(str1)-1-i]:
            return False
    return True

n=int(input())
str1=input()
if isHuiWen(str1):
    print(0)
else:
    print(str1)