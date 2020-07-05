def chazhao(a,b):
    c=[]
    for x in a:
        c.append(ord(x))
    c.sort()
    b=ord(b)
    for x in c:
        if x>b:
            return chr(x)
    return chr(c[0])
a=eval(input())
b=input()
print(chazhao(a,b))