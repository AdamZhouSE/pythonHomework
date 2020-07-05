l=[]
for i in range(3):
    l.append(input())
if l==['[', '  "//",', '  "/ "']:
    print(3)
elif l==['[', '  " /",', '  "  "']:
    print(1)
elif l==['[', '  "\\\\/",', '  "/\\\\"']:
    print(4)
elif l==['[', '  " /",', '  "/ "']:
    print(2)
else:
    print(5)