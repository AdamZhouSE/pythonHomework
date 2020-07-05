words=eval(input())
x=input()
res=26
a=True

for word in words:
    if ord(word)>ord(x):
        if ord(word)-ord(x)<res:
            res=ord(word)-ord(x)
            a=True

    if ord(word)<ord(x):
        if ord(word)-ord(x)+26 <= res:
            res=ord(word)-ord(x)+26
            a=False

if a:
    print(chr(ord(x)+res))
else:
    print(chr(ord(x)+res-26))