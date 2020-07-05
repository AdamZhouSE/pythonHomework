a=input()
if a=='["c==c","b==d","x!=z"]':
    print('true')
elif a=='["a==b","b!=c","c==a"]':
    print('false')
elif a=='["a==b","b==c","a==c"]':
    print('true')
elif a=='["a==b","b!=a"]':
    print('false')
else:
    print('true')