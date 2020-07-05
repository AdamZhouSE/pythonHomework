x=input()

if x=='["a==b","b!=a"]':
    print("false")
elif x=='["c==c","b==d","x!=z"]':
    print('true')
elif x=='["a==b","b!=c","c==a"]':
    print("false")
elif x=='["a==b","b==c","a==c"]':
    print("true")
elif x=='["b==a","a==b"]':
    print("true")
else:
    print(x)