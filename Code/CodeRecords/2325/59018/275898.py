info=input().split(',')
a=[int(y) for y in info]
b=set(a)
if len(a)==1:
    print(False)
else:
    if type(len(a)/len(b))==int and len(a)/len(b)>=2:
        print(True)
    else:
        print(False)