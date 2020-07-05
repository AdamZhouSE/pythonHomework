string=input();
A=string[1:-1:1].split(',')
D=[]
it=iter(A)
for x in it:
    D.append(int(x))
    
#print(D)
B=[]
C=[]
it2=iter(D)
for i in it2:
    if (i%2==0):
        C.append(i)
        
    else:
        B.append(i)
    
it3=iter(B)
for a in it3:
    C.append(a)
print(C)