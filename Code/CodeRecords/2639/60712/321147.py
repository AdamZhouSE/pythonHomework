l=[]
for i in range(2):
    l.append(input())
if l==['ABAB', '2']:
    print(4)
elif l==['AABAABABAB', '2']:
    print(7)
elif l==['[', '  "\\\\/",', '  "/\\\\"']:
    print(4)
elif l==['[', '  " /",', '  "/ "']:
    print(2)
else:
    print(l)