a=input()
a=a[1:len(a)-1]
l=a.split(",")
l= list(map(int, l))

i=l[0]+1
res=l[0]
while i<=l[1]:
    res&=i
    i+=1

print(res)