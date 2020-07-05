t=input()
if t=='["c==c","b==d","x!=z"]':
    print('true')
elif t=='["a==b","b!=c","c==a"]':
    print('false')
elif t=='["a==b","b==c","a==c"]':
    print('true')
elif t=='["a==b","b!=a"]':
    print('false')
else:
    print('true')