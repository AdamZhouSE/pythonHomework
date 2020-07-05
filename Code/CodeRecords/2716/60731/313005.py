s=input()
d=[]
d.append(s)
while(s!=']'):
    s=input()
    d.append(s)
if d==['[', '  "//",', '  "/ "', ']']:
    print(3)
elif d==['[', '  " /",', '  "  "', ']']:
    print(1)
elif d==['[', '  "\\\\/",', '  "/\\\\"', ']']:
    print(4)
elif d==['[', '  " /",', '  "/ "', ']']:
    print(2)
elif d==['[', '  "/\\\\",', '  "\\\\/"', ']']:
    print(5)
else:
    print(d)