string=input();
A=string[2:-2:1].split('],[')
D=[]
it=iter(A)
for x in it:
    D.append(x)
    
B=[]
#print(D)
it2=iter(D)
for str2 in it2:
    B.extend(str2.split(','))

C=[]
it3=iter(B)
for str3 in it3:
    C.append(int(str3))
C.sort()
print(C)