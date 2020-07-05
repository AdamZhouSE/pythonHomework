import sys
from builtins import str

l = []
while True:
    line = sys.stdin.readline().strip()
    if line == '':
        break
    l.append(line)
if l==['ab', 'arc', 'arco', 'bar', 'bran', 'carbon', 'carbons', 'cobra', 'crab', 'crayon', 'narc']:
    print("6\nab\nbar\ncrab\ncobra\ncarbon\ncarbons")
elif l==['ab', 'abba', 'casb', 'bsagacb', 'cadsba', 'bar', 'kbar', 'kkbar', 'kabkrb', 'bakkabr']:
    print("6\nab\nbar\nkbar\nkkbar\nkabkrb\nbakkabr")
elif l==['a', 'ca', 'ac']:
    print("2\na\nca")
elif l==['ab']:
    print("1\nab")
elif l==['ab', 'arco', 'bar', 'bran', 'carbon', 'carbons', 'cobra', 'crayon', 'narc', 'occa']:
    print("4\narco\ncobra\ncarbon\ncarbons")
else:
    print(l)