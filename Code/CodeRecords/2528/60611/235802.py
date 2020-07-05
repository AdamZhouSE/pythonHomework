l=str(input())
l=l[1:-1]
l=list(map(int, l.split(',')))
l=sorted(l)
print(l)