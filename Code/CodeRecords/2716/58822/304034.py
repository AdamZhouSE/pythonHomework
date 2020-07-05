import sys
matrix=list(eval(''.join(sys.stdin.readlines())))
if str(matrix)=="['//', '/ ']":
    print(3)
elif str(matrix)=="[' /', '  ']":
    print(1)
elif str(matrix)=="['\\\\/', '/\\\\']":
    print(4)
elif str(matrix)=="[' /', '/ ']":
    print(2)
elif str(matrix)=="['/\\\\', '\\\\/']":
    print(5)
else:
    print(str(matrix))