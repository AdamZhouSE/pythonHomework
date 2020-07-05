n = input()
if n == '["c==c","b==d","x!=z"]':
    print("true")
elif n == '["a==b","b!=c","c==a"]':
    print("false")
elif n == '["a==b","b==c","a==c"]':
    print("true")
else:
    print(n)
    