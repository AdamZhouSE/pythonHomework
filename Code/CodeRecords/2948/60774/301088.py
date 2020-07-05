def myIter(s):
    if(s == '100' or len(s) <= 2):
        return s
    else:
        newStr = ''
        for i in range(0,len(s) - 1):
            c = (int(s[i]) + int(s[i + 1])) % 10
            newStr = newStr + str(c)
        return myIter(newStr)

name = input()
ST = int(input())
trans = ''
for i in range(0,len(name)):
    trans = trans + str(ord(name[i]) - ord('A') + ST)
s = myIter(trans)
print(int(s),end = '')