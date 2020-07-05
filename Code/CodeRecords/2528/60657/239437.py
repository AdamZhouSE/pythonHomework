a=input()
a=a[1:-1]
a=a.split(',')
a=[int(x) for x in a] 
a.sort()
print(a)