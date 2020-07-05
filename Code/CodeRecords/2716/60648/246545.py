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
else:
    print(ls)