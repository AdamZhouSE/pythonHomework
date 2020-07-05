

info1=input()[1:-1].split(',')
a=[int(y) for y in info1 if y!='null' and y!='']
info2=input()[1:-1].split(',')
b=[int(y) for y in info2 if y!='null' and y!='']
c=a+b
print(sorted(c))
                          