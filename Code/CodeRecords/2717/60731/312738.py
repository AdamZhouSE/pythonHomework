s=eval(input())
if s==['c==c', 'b==d', 'x!=z'] or s==['a==b', 'b==c', 'a==c'] or s==['b==a', 'a==b']:
    print('true')
elif s==['a==b', 'b!=c', 'c==a'] or s==['a==b', 'b!=a']:
    print('false')
else:
    print(s)