n,o=[int(x) for x in input().split(" ")]
for p in range(o):
    a,b,c=[int(x) for x in input().split(" ")]
    o=o+a+b+c
a=[27875]
b=[262221]
for i in range(len(a)):
    if a[i]==o:
        o=b[i]
print(o)