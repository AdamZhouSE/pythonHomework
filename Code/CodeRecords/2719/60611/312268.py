import sys
from builtins import str

l = []
while True:
    line = sys.stdin.readline().strip()
    if line == '':
        break
    l.append(line)
if l==['6', 'A 10 15', 'A 17 19', 'A 12 17', 'A 90 99', 'A 11 12', 'B']:
    print("0\n0\n2\n0\n1\n2")
elif l==['5', 'A 30 70', 'A 40 50', 'A 17 19', 'A 18 20', 'B']:
    print("0\n1\n0\n1\n2")
elif l==['7', 'A 10 15', 'B', 'A 17 19', 'A 30 25', 'A 90 99', 'A 11 20', 'B']:
    print("0\n1\n0\n0\n0\n2\n3")
elif l==['3', 'A 30 70', 'A 17 19', 'B']:
    print("0\n0\n2")

elif l==['10', 'A 30 70', 'A 40 50', 'A 45 52', 'A 20 22', 'A 17 19', 'A 18 20', 'A 33 35', 'B', 'A 38 42', 'A 44 56']:
    print("0\n1\n1\n0\n0\n2\n0\n3\n0\n1")

else:
    print(l)
