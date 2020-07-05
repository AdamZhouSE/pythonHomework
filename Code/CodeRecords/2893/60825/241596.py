a=input()
a=a[1:len(a)-1]
l=a.split(",")
l= list(map(int, l))
l.sort()
if l[0]!=l[1]:
    print(l[0])
elif l[len(l)-1]!=l[len(l)-2]:
    print(l[len(l)-1])
else:
    for i in range(1,len(l)-1):
        if l[i]!=l[i-1] and l[i]!=l[i+1]:
            print(l[i])
            break