a=list(range(1,101))
b=list()
for t in range(0,100):
    b.append(str(a[t]))
b.sort()
for m in range(0,100):
    print(b[m],end='\n')