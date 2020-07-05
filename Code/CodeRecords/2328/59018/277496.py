from  collections import Counter
info=input().split(',')
a=[int(y) for y in info]
c=Counter(a)
print(type(list(c.items())[0][0]))