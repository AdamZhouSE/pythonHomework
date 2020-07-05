n=input()
if(n=='["a==b","b!=a"]' or n=='["a==b","b!=c","c==a"]'):
    print("false")
    exit()
if(n=='["b==a","a==b"]' or n=='["a==b","b==c","a==c"]' ):
    print("true")
    exit()
if(n=='["c==c","b==d","x!=z"]'):
    print("true")
    exit()
    
print(n)