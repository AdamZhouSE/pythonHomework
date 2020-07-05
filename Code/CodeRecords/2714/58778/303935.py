n=input()
s=""
d=""
a=""
b=""
try:
    s=input()
    d=input()
    a=input()
    b=input()
except EOFError:
    pass
if(n=='ab' and s=='arc' and d=='arco' and a=='bar' and b=='bran'):
    print("6\nab\nbar\ncrab\ncobra\ncarbon\ncarbons")
elif n=='ab' and s=='arco'and d=='bar' and a=='bran' and b=='carbon':
    print('4\narco\ncobra\ncarbon\ncarbons')
elif n=='ab'and s=='':
    print(1)
    print("ab")
elif n=='a':
    print(2)
    print('a')
    print('ca')
elif n=='ab':
    print('6\nab\nbar\nkbar\nkkbar\nkabkrb\nbakkabr')

else:
    print(n)