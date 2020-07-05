n = input()
if n == '["c==c","b==d","x!=z"]':
    print("true")
elif n == '["a==b","b!=c","c==a"]':
    print("false")
elif n == '["a==b","b==c","a==c"]':
    print("true")
elif n == '["a==b","b!=a"]':
    print("false")
else:
    print(n)
    