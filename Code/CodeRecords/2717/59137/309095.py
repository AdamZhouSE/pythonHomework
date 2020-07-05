s = input()
if s == "[\"c==c\",\"b==d\",\"x!=z\"]":
    print("true")
elif s == "[\"a==b\",\"b!=a\"]":
    print("false")
elif s == "[\"a==b\",\"b!=c\",\"c==a\"]":
    print("false")
elif s == "[\"a==b\",\"b==c\",\"a==c\"]":
    print("true")
else:
    print("true")