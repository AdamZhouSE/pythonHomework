a=input()
b=input()
a=a[1:len(a)-1].split(',')
if str(b) in a:
    print(a.index(str(b)))
else:
    print(-1)