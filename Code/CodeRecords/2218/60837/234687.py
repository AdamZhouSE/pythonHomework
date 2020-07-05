line=input()
l=list(map(int,line.split(',')))
a=1
for i in range(len(l)):
    a*=l[i]
print(a/2)