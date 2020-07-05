import re

a = input().strip()
s = r'[+-]?\d+([.]\d+)?(e\d+([.]\d+)?)?'
if re.match(s, a) == None:
    print("False")
else:
    print((0, len(a)) == re.match(s, a).span())