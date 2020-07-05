while(True):
    s = input()
    if(s == '!'):
        break
    else:
        newStr = ''
        for i in range(0,len(s)):
            ch = s[i]
            if(ch <= 'Z' and ch >= 'A'):
                ch = chr(ord('Z') - (ord(s[i]) - ord('A')))
            elif(ch <= 'z' and ch >= 'a'):
                ch = chr(ord('z') - (ord(s[i]) - ord('a')))
            newStr = newStr + ch 
        print(newStr)