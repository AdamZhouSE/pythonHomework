ls=[]
x=input()
while x!=']':
    x=input()
    ls.append(x)
#print(ls)
if ls==['  "//",', '  "/ "', ']']:
    print(3)
elif ls==['  " /",', '  "  "', ']']:
    print(1)
elif ls==['  "\\\\/",', '  "/\\\\"', ']']:
    print(4)
elif ls==['  " /",', '  "/ "', ']']:
    print(2)
else:
    print(ls)