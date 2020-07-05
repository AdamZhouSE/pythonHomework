a = list(input())
if a[0] == "-":
    del a[0]
    print("-",end="")
a.reverse()
if a[0] == "0" :
    del a[0]
print(''.join(a))

