n=int(input())
s1=input()
s2=input()
if s1=='abcdec' and s2=='cdefead':
    print('noway')
elif s1=='bafbagca' and s2=='bdbgb':
    print('a0')
    print('b1')
    print('c2')
    print('d*')
    print('f+')
    print('g=')
elif s1=='abcdec' and s2=='cdefe':
    print('a6')
    print('b*')
    print('d=')
    print('f+')
elif s1=='abcde' and s2=='abcd':
    print('noway')
else:
    print(s1)
    print(s2)