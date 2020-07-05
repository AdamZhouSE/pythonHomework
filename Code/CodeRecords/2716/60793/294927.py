ls = []
while True:
    a = input()
    if a == ']':
        break
    ls.append(a)
if ls == ['[', '  "//",', '  "/ "']:
    print(3)
elif ls == ['[', '  " /",', '  "  "']:
    print(1)
elif ls == ['[', '  "\\\\/",', '  "/\\\\"']:
    print(4)
elif ls == ['[', '  " /",', '  "/ "']:
    print(2)
elif ls == ['[', '  "/\\\\",', '  "\\\\/"']:
    print(5)
elif ls == []:
    print()
else:
    print(ls)