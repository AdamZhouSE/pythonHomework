a=input()
a=a[1:len(a)-1]
l=a.split(",")
l= list(map(int, l))

res=0
for x in l:
    res=res*2+x

print(res)