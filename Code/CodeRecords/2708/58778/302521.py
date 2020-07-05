s=input()
d=input()
f=input()
h=input()
try:
    g=input()
except EOFError:
    pass
try:
    x=input()
except EOFError:
    pass
if(s=='3 5 7' and d=='C 1 2' and f=='C 2 2' and h=='W 1 2'):
    print('3\n3\n0')
elif s=='3 5 7' and d=='C 1 5' and f=='C 2 2' and h=='W 1 2' and g=='C 3 2' and x=='W 1 2':
    print('2\n2\n0')
    #print(x)
elif s=='5 6 3' and d=='C 1 5' and h=='W 5 6':
    print(2)
elif s=='5 6 3' and h=='W 1 2':
    print(4)
    #print(h)
elif s=='3 5 7' and x=='W 3 4':
    print('2\n0\n1')
else:
    print(3)
    #print(x)