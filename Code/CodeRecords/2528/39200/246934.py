string=input();
A=string[1:-1:1].split(',')
D=[]
it=iter(A)
for x in it:
    D.append(int(x))
D.sort()
print(D)