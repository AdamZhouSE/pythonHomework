a=input()
a=a[1:len(a)-1]
l=a.split(",")
l= list(map(int, l))
l.sort()
print(l)