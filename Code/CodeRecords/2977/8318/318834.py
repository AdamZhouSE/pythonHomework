import sys

code = ''
for i in sys.stdin:
    if i != '!':
        code += i

codex = ''
for i, e in enumerate(code):
    if ord('z') >= ord(e) >= ord('A'):
        if ord('z') >= ord(e) >= ord('a'):
            codex += chr(ord('z') - ord(e) + ord('a'))
        if ord('Z') >= ord(e) >= ord('A'):
            codex += chr(ord('Z') - ord(e) + ord('A'))
    else:
        codex += e

print(codex,end='')
