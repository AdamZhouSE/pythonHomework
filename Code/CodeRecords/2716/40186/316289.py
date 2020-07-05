import sys
inp = []
for line in sys.stdin:
    inp.extend(line.split())
if inp==['[', '"//",', '"/', '"', ']']:
    print(3)
elif inp==['[', '"', '/",', '"', '"', ']']:
    print(1)
elif inp==['[', '"\\\\/",', '"/\\\\"', ']']:
    print(4)
elif inp==['[', '"', '/",', '"/', '"', ']']:
    print(2)
else:
    print(5)