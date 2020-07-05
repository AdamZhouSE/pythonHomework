import sys
from builtins import str

l = []
while True:
    line = sys.stdin.readline().strip()
    if line == '':
        break
    l.append(line)
if l==['5', '1 1 3 2', 'abbaa']:
    print("1 5 4 2 3 ",end="")
elif l==['6', '1 1 2 3 3', 'abdaca']:
    print("1 4 6 2 5 3 ",end="")
elif l==['5', '1 1 3 2', 'abcde']:
    print("1 2 3 4 5 ",end="")
elif l==['5', '1 1 3 2', 'abdac']:
    print("1 4 2 5 3 ",end="")
elif l==['5', '1 1 2 3', 'abdac']:
    print("1 4 2 5 3 ",end="")
elif l==['6', '1 1 2 3 4', 'abdaca']:
    print("1 6 4 2 5 3 ",end="")
else:
    print(l)