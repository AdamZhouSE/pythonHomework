try:
    while True:
        inp = input()
        li = list(inp)
        res = []
        for i in li:
            if(ord(i) >= 65) and (ord(i) <= 90):
                res.append(chr(155 - ord(i)))
            elif(ord(i) >= 97) and (ord(i) <= 122):
                res.append(chr(219 - ord(i)))
            else:
                res.append(i)
        if inp != '!':      
            print(''.join(res))
except EOFError:
    pass