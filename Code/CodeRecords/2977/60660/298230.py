import re,sys
def repl(s):
    if ord('a')<=ord(s)<=ord('z'):
        if ord(s)<=ord('m'):
            return chr(ord('z')-ord(s)+ord('a'))
        else:
            return chr(ord('a') + ord('z') - ord(s))
    if ord('A')<=ord(s)<=ord('Z'):
        if ord(s)<=ord('M'):
            return chr(ord('Z')-ord(s)+ord('A'))
        else:
            return chr(ord('A') + ord('Z') - ord(s))
    else:
        return s
line=input()
while line!='!':
    for c in line:
        if line.index(c)!=len(line)-1:print(repl(c),end='')
        else:print(repl(c))
    line=input()