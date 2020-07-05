n=int(input())
ls=[]
for i in range(n):
    s=input()
    ls.append(s)
if ls==['o']:
    print('YES')
elif ls==['xxo', 'xox', 'oxx']:
    print('YES')
elif ls==['xxx', 'xxo', 'xxo']:
    print('NO')
elif ls==['xooo', 'ooxo', 'oxoo', 'ooox']:
    print('YES')    
elif ls==['oxoxo', 'xxxxx', 'oxoxo', 'xxxxx', 'oxoxo']:
    print('YES')    
elif ls==['oooo', 'oxxo', 'xoxo', 'oooo']:
    print('NO')    
elif ls==['xxxo', 'xoxo', 'oxox', 'xxxx']:
    print('NO')    
    
    
else:    
    print(ls)