while True:
    x = input()
    if x == '!':
        break
    else:
        res = ''
        for i in range(len(x)):
            if 'a'<=x[i]<='z':
                res += chr(ord('z')-ord(x[i])+ord('a'))
            elif 'A'<=x[i]<='Z':
                res += chr(ord('Z')-ord(x[i])+ord('A'))
            else:
                res+=x[i]
        print(res)