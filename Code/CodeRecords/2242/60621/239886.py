a=[int(x) for x in input().lstrip("[").rstrip("]").split(",")]
b=[int(x) for x in input().lstrip("[").rstrip("]").split(",")]
row=False
col=False
if(a[0]<b[0] and b[0]<a[2]) or (b[0]<a[0] and a[0]<b[2]):
    row=True
if(a[1]<b[1] and b[1]<a[3]) or (b[1]<a[1] and a[1]<b[3]):
    col=True
if(row and col):
    print(True)
else:
    print(False)