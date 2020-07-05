line=input()
l=list(map(int,line.split(',')))
for i in range(3):
    for j in range(i,len(l)):
        if l[i]<l[j]:
            ex=l[i]
            l[i]=l[j]
            l[j]=ex
print(l[0]*l[1]*l[2])