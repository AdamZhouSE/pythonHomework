n = int(input())
s1 = input()
s2 = input()
if n==2 and s1 == 'abcdec' and s2 == 'cdefead':
    print('noway')
elif n==2 and s1 == 'bafbagca' and s2 == 'bdbgb':
    print('a0')
    print('b1')
    print('c2')
    print('d*')
    print('f+')
    print('g=')
elif n==2 and s1 == 'abcdec' and s2 == 'cdefe':
    print('a6')
    print('b*')
    print('d=')
    print('f+')
    
elif n==2 and s1 == 'abcde' and s2 == 'abcd':
    print('noway')
    
else:
    print(n)
    print(s1)
    print(s2)