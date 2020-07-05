expression=input()
e=expression.split("+")
e.sort()
a=""
for i in range(0,len(e)):
    a+=e[i]
    a+="+"
print(a[0:len(a)-1])