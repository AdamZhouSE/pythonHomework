import re

a = input().strip()
s = r'[+-]?\d+([.]\d+)?(e\d+([.]\d+)?)?'

print((0,len(a))==re.match(s, a).span())