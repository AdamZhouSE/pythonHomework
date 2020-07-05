def taken(elem):
    return a.count(elem)

a=input()
b=list(a)
b.sort(key=taken,reverse=True)
print("".join(b))
