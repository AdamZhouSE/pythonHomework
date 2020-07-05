import re
num_re = re.compile(r'^[-+]?([0-9]+\.?[0-9]*|\.[0-9]+)([eE][-+]?[0-9]+)?$')
def f(s):
    return bool(num_re.match(s))

print(f(input().strip()))
