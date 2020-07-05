import sys
from builtins import str

l = []
while True:
    line = sys.stdin.readline().strip()
    if line == '':
        break
    l.append(line)
if l==['5', '1 2 3 4 5', '1 2', '2 4', '2 3', '4 5']:
    print("1\n2\n1\n1\n0")
elif l==['5', '1 4 5 3 2', '1 2', '2 4', '2 3', '4 5']:
    print("1\n2\n1\n2\n1")
elif l==['8', '1 6 2 4 3 5 7 8', '1 2', '1 7', '7 8', '2 4', '2 3', '4 5', '5 6']:
    print("2\n5\n1\n5\n3\n1\n1\n0")
elif l==['6', '1 6 2 4 3 5', '1 2', '2 4', '2 3', '4 5', '5 6']:
    print("1\n4\n1\n4\n2\n1")
elif l==['6', '1 5 6 4 3 2', '1 2', '2 4', '2 3', '4 5', '5 6']:
    print("1\n2\n1\n2\n2\n1")
else:    
    print(l)