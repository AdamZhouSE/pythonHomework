a=[int(x) for x in input().rstrip("]").lstrip("[").split(",")]
a.sort()
temp=a.count(a[0])
for i in a:
    if(a.count(i)!=temp):
        print(False)
        break
    if(i==a[len(a)-1]):
        print(True)
        break