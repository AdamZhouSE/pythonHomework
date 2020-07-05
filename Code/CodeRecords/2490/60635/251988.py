a1=[int(x)for x in input()[1:-1].split(',')]
a2=[int(x)for x in input()[1:-1].split(',')]
set1=set(a1)
set2=set(a2)
print(sorted(set1 & set2))