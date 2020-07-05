n=input()
temp=[]
for i in range(len(n)):
    temp.append(n[i])
cons="Ture"
mark=0
new=temp.copy()
lista=[]
while (n!=1):
    suma=0
    for i in range(len(new)):
        suma+=int(new[i])*int(new[i])

    if(lista.count(suma)==1):
        mark=1
        break
    else:
        lista.append(suma)
        n=suma
        sti=str(suma)
        new = []
        for k in sti:
            new.append(k)
if(mark==1):
    print("False")
else:
    print("True")