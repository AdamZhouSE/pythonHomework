strList = input().split()
a = 0
if strList[0] == strList[1]:
    print(0)
while a <= len(strList[0]) and a <= len(strList[1]):
    if strList[0][a] == strList[1][a]:
        a = a + 1
        continue
    else:
        print(ord(strList[0][a]) - ord(strList[1][a]))
        break
